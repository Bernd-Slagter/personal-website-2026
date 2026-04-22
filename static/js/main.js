// ── Theme ──────────────────────────────────────────────────────────────────

const systemDark = window.matchMedia('(prefers-color-scheme: dark)');

function applyTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
}

function resolveTheme() {
  const saved = localStorage.getItem('theme');
  return saved || (systemDark.matches ? 'dark' : 'light');
}

applyTheme(resolveTheme());

const themeToggle = document.getElementById('themeToggle');
if (themeToggle) {
  themeToggle.addEventListener('click', () => {
    const next = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    localStorage.setItem('theme', next);
    applyTheme(next);
  });
}

// Follow system preference changes only when the user hasn't made a manual choice
systemDark.addEventListener('change', e => {
  if (!localStorage.getItem('theme')) {
    applyTheme(e.matches ? 'dark' : 'light');
  }
});

// ── Mobile nav ─────────────────────────────────────────────────────────────

const navToggle = document.getElementById('navToggle');
const navLinks  = document.getElementById('navLinks');
if (navToggle) {
  navToggle.addEventListener('click', () => navLinks.classList.toggle('open'));
}

// ── Scroll-to-top ──────────────────────────────────────────────────────────

const scrollBtn = document.getElementById('scrollTop');
if (scrollBtn) {
  window.addEventListener('scroll', () => {
    scrollBtn.classList.toggle('visible', window.scrollY > 300);
  });
  scrollBtn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
}

// ── Skill bar animation ────────────────────────────────────────────────────

const barObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.width = entry.target.dataset.width + '%';
      barObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.2 });

document.querySelectorAll('.skill-fill').forEach(bar => {
  bar.style.width = '0%';
  barObserver.observe(bar);
});

// ── Active nav link ────────────────────────────────────────────────────────

const path = window.location.pathname;
document.querySelectorAll('.nav-links a').forEach(link => {
  const href = link.getAttribute('href');
  if (href === path || (href !== '/' && path.startsWith(href))) {
    link.classList.add('active');
  }
});
