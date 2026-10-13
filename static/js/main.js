// Site-wide scripts. Page-specific scripts go in each template's extra_js block.

// Eye button to show / hide every password field
document.querySelectorAll('input[type="password"]').forEach(input => {
    const wrapper = document.createElement('div');
    wrapper.className = 'password-field';
    input.before(wrapper);
    wrapper.append(input);
    wrapper.insertAdjacentHTML('beforeend', '<button type="button" class="password-toggle" aria-label="Show password"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg></button>');
    wrapper.lastChild.onclick = () => input.type = input.type === 'password' ? 'text' : 'password';
});
