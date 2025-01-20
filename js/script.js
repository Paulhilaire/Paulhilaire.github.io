document.addEventListener('DOMContentLoaded', function() {
    const lists = document.querySelectorAll('.continuous-list');
    let startNumber = 1;

    lists.forEach(list => {
        list.setAttribute('start', startNumber);
        startNumber += list.querySelectorAll('li').length;
    });
});