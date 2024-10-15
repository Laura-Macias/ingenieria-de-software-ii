const carouselTrack = document.querySelector('.carousel-track');
const totalSlides = document.querySelectorAll('.carousel-track img').length;
let currentSlide = 1; // Empezamos en la primera imagen real
const slideWidth = 50; // Cada slide ocupa el 50% del contenedor (para mostrar 2 imágenes)

carouselTrack.style.transform = `translateX(${-slideWidth}%)`; // Colocamos el carrusel en la primera imagen real

function moveCarousel() {
    currentSlide++;
    
    // Aplicamos la transición suave cuando pasamos entre las imágenes reales
    carouselTrack.style.transition = 'transform 0.5s ease';
    carouselTrack.style.transform = `translateX(${-(slideWidth * currentSlide)}%)`;

    // Si estamos en la imagen clonada (última slide), hacemos el "salto" a la primera imagen real
    if (currentSlide === totalSlides - 1) {
        setTimeout(() => {
            // Desactivamos la transición temporalmente para hacer el salto invisible
            carouselTrack.style.transition = 'none';
            currentSlide = 1; // Saltamos a la primera imagen real
            carouselTrack.style.transform = `translateX(${-slideWidth}%)`;
        }, 500); // El tiempo de la transición antes de hacer el salto
    }
}

// Mover el carrusel cada 3 segundos
setInterval(moveCarousel, 3000);

// Reiniciar la transición cuando el usuario navegue manualmente (si hay botones)
carouselTrack.addEventListener('transitionend', () => {
    // Si estamos en el último clon, saltamos al primero
    if (currentSlide === totalSlides - 1) {
        carouselTrack.style.transition = 'none';
        currentSlide = 1;
        carouselTrack.style.transform = `translateX(${-slideWidth}%)`;
    }
});
