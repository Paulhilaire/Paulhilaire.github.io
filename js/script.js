document.addEventListener('DOMContentLoaded', function() {
    const lists = document.querySelectorAll('.continuous-list');
    let startNumber = 1;

    lists.forEach(list => {
        list.setAttribute('start', startNumber);
        startNumber += list.querySelectorAll('li').length;
    });
});

// document.querySelector('.read-more-btn').addEventListener('click', function () {
//     const fullText = document.querySelector('.full-text');
//     const shortText = document.querySelector('.short-text');
//     if (fullText.style.display === 'none') {
//         fullText.style.display = 'block';
//         shortText.style.display = 'none';
//         this.textContent = 'Read less'; // Change button text
//     } else {
//         fullText.style.display = 'none';
//         shortText.style.display = 'block';
//         this.textContent = 'Read more'; // Reset button text
//     }
// });

document.querySelectorAll('.read-more-btn').forEach(button => {
    button.addEventListener('click', function () {
        const fullText = this.closest('.right').querySelector('.full-text');
        const shortText = this.closest('.right').querySelector('.short-text');
        
        if (fullText.style.display === 'none') {
            fullText.style.display = 'block';
            shortText.style.display = 'none';
            this.textContent = 'Read less'; // Change button text
        } else {
            fullText.style.display = 'none';
            shortText.style.display = 'block';
            this.textContent = 'Read more'; // Reset button text
        }
    });
});
