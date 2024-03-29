const imageElement = document.querySelector('div.profile-photo > img');
const formElement = document.querySelector('div.profile-photo-form');
const changePhotoLinkElement = document.querySelector('a.change-photo-link');

if (imageElement.src === '') {
    formElement.style.display = 'block';
} else {
    formElement.style.display = 'none';
}

changePhotoLinkElement.addEventListener('click', () => {
    if (formElement.style.display === 'none') {
        formElement.style.display = 'block';
    } else {
        formElement.style.display = 'none'
    }
})
