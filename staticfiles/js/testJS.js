function toggleOption(element) {
    const option = element.parentElement;
    option.classList.toggle('active');

    const content = option.querySelector('.option-content');
    if (option.classList.contains('active')) {
        content.style.maxHeight = content.scrollHeight + 'px';
    } else {
        content.style.maxHeight = 0;
    }
}
