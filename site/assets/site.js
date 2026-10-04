(() => {

  const navToggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('#site-nav');
  if (navToggle && nav) {
    navToggle.addEventListener('click', () => {
      const open = navToggle.getAttribute('aria-expanded') === 'true';
      navToggle.setAttribute('aria-expanded', String(!open));
      nav.classList.toggle('open', !open);
      if (!open) nav.querySelector('a')?.focus();
    });
  }

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && navToggle?.getAttribute('aria-expanded') === 'true') {
      navToggle.setAttribute('aria-expanded', 'false'); nav.classList.remove('open'); navToggle.focus();
    }
  });
  matchMedia('(min-width: 761px)').addEventListener('change', () => {
    navToggle?.setAttribute('aria-expanded', 'false'); nav?.classList.remove('open');
  });

  const currentPath = window.location.pathname.replace(/index\.html$/, '');
  document.querySelectorAll('.docs-nav a').forEach((link) => {
    const linkPath = new URL(link.href).pathname.replace(/index\.html$/, '');
    if (linkPath === currentPath) link.setAttribute('aria-current', 'page');
  });

  document.querySelectorAll('.prose pre').forEach((pre) => {
    const code = pre.querySelector('code');
    if (!code) return;
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'copy-button';
    button.textContent = 'Copy';
    button.setAttribute('aria-label', 'Copy code');
    const feedback = document.createElement('span');
    feedback.className = 'visually-hidden'; feedback.setAttribute('role', 'status');
    pre.tabIndex = 0; pre.setAttribute('aria-label', 'Code example');
    button.addEventListener('click', async () => {
      feedback.textContent = 'Copying code…';
      let timeout;
      try {
        await Promise.race([navigator.clipboard.writeText(code.textContent), new Promise((_, reject) => { timeout = setTimeout(() => reject(new Error('Clipboard timed out')), 1500); })]);
        button.textContent = 'Copied'; feedback.textContent = 'Code copied to clipboard.';
      } catch (_) {
        button.textContent = 'Select text'; feedback.textContent = 'Copy unavailable. Select the code text.';
      } finally { clearTimeout(timeout); }
      window.setTimeout(() => { button.textContent = 'Copy'; }, 1600);
    });
    pre.append(button, feedback);
  });

  document.querySelectorAll('.prose table').forEach(table => { table.tabIndex = 0; });

  const form = document.querySelector('[data-search-form]');
  if (!form) return;
  const input = form.querySelector('input');
  const results = document.querySelector('[data-search-results]');
  const status = document.querySelector('[data-search-status]');
  let indexPromise;
  let searchSequence = 0;

  const loadIndex = () => {
    if (!indexPromise) indexPromise = fetch(form.dataset.index).then((response) => {
      if (!response.ok) throw new Error('Search index unavailable');
      return response.json();
    });
    return indexPromise;
  };
  const excerpt = (text, term) => {
    const normalized = text.replace(/\s+/g, ' ').trim();
    const at = normalized.toLowerCase().indexOf(term);
    const start = Math.max(0, at - 65);
    const end = Math.min(normalized.length, start + 180);
    return `${start ? '…' : ''}${normalized.slice(start, end)}${end < normalized.length ? '…' : ''}`;
  };
  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const thisSearch = ++searchSequence;
    const term = input.value.trim().toLowerCase();
    results.replaceChildren();
    if (term.length < 2) { status.textContent = 'Enter at least two characters.'; return; }
    status.textContent = 'Searching documentation…';
    try {
      const pages = await loadIndex();
      if (thisSearch !== searchSequence) return;
      const matches = pages.filter((page) => `${page.title} ${page.text}`.toLowerCase().includes(term)).slice(0, 8);
      status.textContent = matches.length ? `${matches.length} result${matches.length === 1 ? '' : 's'}.` : `No documentation found for “${input.value.trim()}”.`;
      matches.forEach((page) => {
        const item = document.createElement('li');
        const link = document.createElement('a');
        link.href = page.url;
        link.textContent = page.title;
        const summary = document.createElement('p');
        summary.textContent = excerpt(page.text, term);
        item.append(link, summary);
        results.appendChild(item);
      });
    } catch (_) {
      indexPromise = undefined;
      if (thisSearch !== searchSequence) return;
      status.textContent = 'Search is unavailable. Use the documentation navigation below.';
    }
  });
  form.querySelector('[data-search-clear]').addEventListener('click', () => {
    searchSequence++;
    input.value = '';
    results.replaceChildren();
    status.textContent = 'Search page titles and documentation text.';
    input.focus();
  });
})();
