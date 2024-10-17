const carouselImages = document.querySelector('.carousel-images');
const totalImages = document.querySelectorAll('.carousel-images img').length;
let currentIndex = -1;

function moveCarousel() {
    currentIndex++;
    if (currentIndex >= totalImages) {
        currentIndex = 0; // Reinicia cuando llega al final
    }
    const offset = -currentIndex * 25; // Cambia la posición del carrusel
    carouselImages.style.transform = `translateX(${offset}%)`;
}

// Cambiar imagen cada 3 segundos
setInterval(moveCarousel, 3500);