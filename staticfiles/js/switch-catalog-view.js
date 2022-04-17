(function () {
  'use strict';

  let modes = document.querySelector('.layout-modes');
  let btnGrid = modes.querySelector('.btn-grid');
  let btnList = modes.querySelector('.btn-list');

  let productGrid = document.querySelectorAll('.product-grid');
  let productList = document.querySelectorAll('.product-list');

  modes.addEventListener('click', (evt) => {
    evt.preventDefault();
    if (evt.target.classList.contains('icon-mode-grid')) {
      switchButtonView(btnGrid, btnList);
      switchProductView(productGrid, productList);
    }
    if (evt.target.classList.contains('icon-mode-list')) {
      switchButtonView(btnList, btnGrid);
      switchProductView(productList, productGrid);
    }
  });

  function switchProductView(first, second) {
    for (let i = 0; i < productGrid.length; i++) {
      first[i].classList.remove('product-hide');
      second[i].classList.add('product-hide');
    }
  }

  function switchButtonView(first, second) {
    first.classList.add('active');
    second.classList.remove('active');
  }

})();