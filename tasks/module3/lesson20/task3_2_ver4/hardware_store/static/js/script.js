
window.onload = function (){
    let attr = undefined
    if (document.title == "Главная страница") {
        attr = document.getElementById('main_ref');
    } else {
        attr = document.getElementById('contacts_ref');
    }
    attr.setAttribute('class', 'active');

    // Получаем элементы для обработки всплывающего окна
    let modal = document.getElementById('successModal');
    let okBtn = document.getElementById('ok_button');
    let closeBtn = document.querySelector('.close');
    let addBtn = document.querySelector('.add-to-cart');

    // Функция для закрытия модального окна
    function closeModal() {
        modal.style.display = 'none';
    }

    // Закрытие модального окна при клике ОК
    okBtn.addEventListener('click', closeModal);

    // Закрытие модального окна при клике на крестик
    closeBtn.addEventListener('click', closeModal);

}



