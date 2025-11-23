
// Функция для форматирования чисел с разрядами
function formatNumber(number) {
    return new Intl.NumberFormat('ru-RU').format(number);
}

window.onload = function (){

    //Задаем выделение в меню для активной страницы
    let attr = undefined
    if (document.title == "Главная страница") {
        attr = document.getElementById('main_ref');
    } else if (document.title == "Контакты") {
        attr = document.getElementById('contacts_ref');
    }
    attr.setAttribute('class', 'active');

    // Получаем элементы для обработки всплывающего окна
    let modal = document.getElementById('successModal');
    let okBtn = document.getElementById('ok_button');
    let closeBtn = document.querySelector('.close');

    // Функция для закрытия модального окна
    function closeModal() {
            modal.style.display = 'none';
    }

    // Закрытие модального окна при клике ОК
    okBtn.addEventListener('click', closeModal);

    // Закрытие модального окна при клике на крестик
    closeBtn.addEventListener('click', closeModal);

}

document.addEventListener('DOMContentLoaded', function() {

    // Функция для обновления данных корзины на странице
    function updateCartData(data) {
        // Обновляем количество товара
        let quantityElement = document.getElementById('quantity-' + data.item_id);
        if (quantityElement) {
            quantityElement.textContent = formatNumber(data.new_quantity);
        }

        // Обновляем сумму для товара
        let sumElement = document.getElementById('sum-' + data.item_id);
        if (sumElement) {
            sumElement.textContent = formatNumber(data.item_sum);
        }

        // Обновляем общую сумму
        let totalSumElement = document.getElementById('total-sum');
        if (totalSumElement) {
            totalSumElement.textContent = formatNumber(data.total_sum);
        }

        // Если товар удален, удаляем строку
        if (data.deleted) {
            const rowElement = document.getElementById('row-' + data.item_id);
            if (rowElement) {
                rowElement.remove();
            }
        }
    }

    // Функция для отправки AJAX запроса
    function sendQuantityRequest(itemId, action) {
        fetch(`/${action}_quantity?item_id=${itemId}`, {
            method: 'POST',
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                updateCartData(data);
            } else {
                alert('Ошибка: ' + data.error);
            }
        })
        .catch(error => {
            alert('Произошла ошибка при обновлении корзины');
        });
    }

    // Обработчики для кнопок увеличения количества
    document.querySelectorAll('.btn-increase').forEach(button => {
        button.addEventListener('click', function() {
            let itemId = this.value;
            sendQuantityRequest(itemId, 'increase');
        });
    });

    // Обработчики для кнопок уменьшения количества
    document.querySelectorAll('.btn-decrease').forEach(button => {
        button.addEventListener('click', function() {
            let itemId = this.value;
            sendQuantityRequest(itemId, 'decrease');
        });
    });


    // Применяем форматирование ко всем элементам с классом 'number'
    let numberElements = document.querySelectorAll('.number');
    numberElements.forEach(element => {
        let number = parseFloat(element.textContent);
        if (!isNaN(number)) {
            element.textContent = formatNumber(number);
        }
    });

    // Применяем форматирование ко всем элементам с классом 'date'
    let dateElements = document.querySelectorAll('.date');
    dateElements.forEach(element => {
        let date = new Date(element.textContent);
        if (!isNaN(date.getTime())) {
            element.textContent = date.toLocaleString('ru-RU');
        }
    });

});



