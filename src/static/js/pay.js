const paymentForm = document.getElementById('payment-form');
const processingDiv = document.getElementById('processing');
const confirmationDiv = document.getElementById('confirmation');
const cardDetails = document.getElementById('card-details');
const pseDetails = document.getElementById('PSE');
const paymentRadios = document.querySelectorAll('input[name="payment"]');
const submitButton = document.querySelector('button[type="submit"]');

// Función para comprobar si todos los campos están llenos según el método de pago seleccionado
function validateForm() {
    let allFieldsFilled = true;
    const selectedPaymentMethod = document.querySelector('input[name="payment"]:checked').value;

    if (selectedPaymentMethod === 'card') {
        // Obtener los valores de los campos de tarjeta
        const cardHolder = document.getElementById('card-holder').value;
        const cardNumber = document.getElementById('card-number').value;
        const cardCVV = document.getElementById('card-cvv').value;
        const cardExpiration = document.getElementById('card-expiration').value;

        // Validar solo los campos de tarjeta si el método seleccionado es 'card'
        if (!cardHolder || !cardNumber || !cardCVV || !cardExpiration) {
            allFieldsFilled = false;
        }
    } else if (selectedPaymentMethod === 'PSE') {
        // Obtener los valores de los campos de PSE
        const pseEmail = document.getElementById('PSE-email').value;
        const pseBank = document.getElementById('PSE-bank').value;

        // Validar solo los campos de PSE si el método seleccionado es 'PSE'
        if (!pseEmail || !pseBank) {
            allFieldsFilled = false;
        }
    }

    // Activar o desactivar el botón de envío según si todos los campos están llenos
    submitButton.disabled = !allFieldsFilled;
}

// Mostrar/ocultar los detalles de cada método de pago según la selección
paymentRadios.forEach(radio => {
    radio.addEventListener('change', () => {
        // Mostrar u ocultar los detalles del método de pago seleccionado
        if (radio.value === 'card') {
            cardDetails.style.display = 'block';
            pseDetails.style.display = 'none';
        } else if (radio.value === 'PSE') {
            cardDetails.style.display = 'none';
            pseDetails.style.display = 'block';
        }
        validateForm(); // Validar después de cambiar el método de pago
    });
});

// Validación de los campos del formulario, asegurándonos de validar solo los campos visibles
document.querySelectorAll('input[type="text"], input[type="email"], input[type="number"], #PSE select').forEach(input => {
    input.addEventListener('input', () => {
        // Solo validamos si el campo pertenece al método de pago visible (card o PSE)
        if ((cardDetails.style.display === 'block' && input.closest('#card-details')) ||
            (pseDetails.style.display === 'block' && input.closest('#PSE'))) {
            validateForm(); // Validar solo si el campo pertenece al método seleccionado
        }
    });
});

// Validación de solo números en los campos de tarjeta y CVV
document.getElementById('card-number').addEventListener('input', function() {
    this.value = this.value.replace(/\D/g, '');  
});

document.getElementById('card-cvv').addEventListener('input', function() {
    this.value = this.value.replace(/\D/g, '');  
});

document.getElementById('card-expiration').addEventListener('input', function() {
    // Eliminar cualquier carácter no numérico o barra
    this.value = this.value.replace(/[^0-9\/]/g, '');

    // Asegurarse de que el formato sea MM/AA (incluso cuando se introduzca el mes)
    if (this.value.length === 2) {
        this.value = this.value + '/'; // Insertar la barra automáticamente
    }
});


// Validar cuando el formulario se envíe
paymentForm.addEventListener('submit', (event) => {
    event.preventDefault();
    if (!submitButton.disabled) {
        paymentForm.style.display = 'none';
        processingDiv.style.display = 'block';

        setTimeout(() => {
            processingDiv.style.display = 'none';
            confirmationDiv.style.display = 'block';
        }, 2000);
    }
});
