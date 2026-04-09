// Theme handler

const root = document.documentElement;
const saved = localStorage.getItem('theme') || 'light';
root.setAttribute('data-theme', saved);

window.onload = function () {
    const icon = document.getElementById('themeIcon');
    if (icon) icon.textContent = (saved === 'dark') ? 'light_mode' : 'dark_mode';
};

function changeTheme() {
    const next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    icon.textContent = (next === 'dark') ? 'light_mode' : 'dark_mode';
}

// End theme handler