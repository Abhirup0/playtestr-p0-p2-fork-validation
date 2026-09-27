// Same pinned terminal SDK and exact Go workspace/state oracle as other tools.
use std::{env, fs, time::Duration};
use termlens::{Key, Terminal};

fn terminal(journey: &str, cols: u16, rows: u16) -> termlens::Result<Terminal> {
    Terminal::builder()
        .size(cols, rows)
        .env_clear()
        .env("PATH", env::var("PATH").expect("PATH"))
        .timeout(Duration::from_secs(10))
        .arg("-journey")
        .arg(journey)
        .arg("-root")
        .arg(env::var("RWX_ROOT").expect("RWX_ROOT"))
        .arg("-variant")
        .arg(env::var("RWX_VARIANT").expect("RWX_VARIANT"))
        .arg("-output")
        .arg(env::var("RWX_RESULT").expect("RWX_RESULT"))
        .spawn(env::var("RWX_LAUNCHER").expect("RWX_LAUNCHER"))
}

fn exact_state() {
    let state = fs::read_to_string(env::var("RWX_RESULT").expect("RWX_RESULT"))
        .expect("independent result");
    assert!(state.contains("\"exit\":0"));
    assert!(state.contains("\"cleaned\":true"));
}

#[test]
fn real_rw1() -> termlens::Result<()> {
    let mut t = terminal("RW1", 120, 40)?;
    t.wait_until(|s| s.contains("alpha.txt"))?;
    t.wait_until(|s| s.contains("beta.txt"))?;
    t.send_str("2")?;
    t.send(Key::Down)?;
    t.wait_until(|s| s.contains("PLAYTESTR-LG alpha changed"))?;
    t.send_str(" ")?;
    t.send_str("\u{3}")?;
    t.wait_until(|s| s.contains("PLAYTESTR-E2-RW1-WRAPPER-OK"))?;
    assert!(t.wait_exit()?.success());
    exact_state();
    Ok(())
}

#[test]
fn real_rw3() -> termlens::Result<()> {
    let mut t = terminal("RW3", 100, 30)?;
    t.wait_until(|s| s.contains("Package name:"))?;
    t.send_str("corrected-package")?;
    t.send(Key::Enter)?;
    t.wait_until(|s| s.contains("Select a framework:"))?;
    t.send(Key::Enter)?;
    t.wait_until(|s| s.contains("Select a variant:"))?;
    t.send(Key::Down)?;
    t.send(Key::Enter)?;
    t.wait_until(|s| s.contains("Install with npm and start now?"))?;
    t.send(Key::Right)?;
    t.send(Key::Enter)?;
    t.wait_until(|s| s.contains("PLAYTESTR-E2-RW3-WRAPPER-OK"))?;
    assert!(t.wait_exit()?.success());
    exact_state();
    Ok(())
}
