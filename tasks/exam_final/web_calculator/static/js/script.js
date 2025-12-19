
// Функция для добавления символа на дисплей
function addToDisplay(value) {
    let display = document.getElementById('display');

    if (display.value === 'Ошибка') {
        display.value = '0';
    }

    // Если текущее значение в дисплее "0", заменяем его
    if (display.value === '0' && value !== '.') {
        display.value = value;
    } else {
        // Проверяем, чтобы операторы не шли подряд
        let lastChar = display.value.slice(-1);
        let operators = ['+', '-', '*', '/', '.'];
        if (operators.includes(lastChar) && operators.includes(value)) {
            // Заменяем последний оператор на новый
            display.value = display.value.slice(0, -1) + value;
        } else {
            display.value += value;
        }
    }
}

// Функция для очистки дисплея
function clearDisplay() {
    document.getElementById('display').value = '0';
}

// Функция для вычисления результата
function calculate() {
    let display = document.getElementById('display');

    try {
        // Заменяем символы для корректного вычисления
        let expression = display.value;
        
        // Проверяем, является ли выражение пустым или содержит только оператор
        if (!expression || /^[+\-*/.]$/.test(expression)) {
            display.value = '0';
            return;
        }
        
        // Проверяем, чтобы выражение не заканчивалось оператором
        if (/[+\-*/.]$/.test(expression)) {
            expression = expression.slice(0, -1);
        }
        
        // Вычисляем выражение
        let result = eval(expression);

        // Проверяем результат на корректность
        if (isNaN(result) || !isFinite(result)) {
            display.value = 'Ошибка';
            return;
        }
        
        // Ограничиваем количество знаков после запятой
        display.value = parseFloat(result.toFixed(10));
        
    } catch (error) {
        display.value = 'Ошибка';
        console.error('Ошибка вычисления:', error);
    }
}

// Функция для удаления последнего символа из дисплея
function deleteLast() {
    let display = document.getElementById('display');
    if (display.value === 'Ошибка') {
        display.value = '0';
    }
    if (display.value.length > 1 && display.value !== '0') {
        display.value = display.value.slice(0, -1);
    } else {
        display.value = '0';
    }
}