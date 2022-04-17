(function () {
  'use strict';

  let addressBoxes = document.querySelectorAll('.shipping-address-box');
  addressBoxes[0].classList.add('active');

  for (let i = 0; i < addressBoxes.length; i++) {
    addressBoxes[i].addEventListener('click', (evt) => {
      evt.preventDefault();
      if (evt.target.classList.contains('ship-here')) {
        deactiveAllAddressBoxes();
        addressBoxes[i].classList.add('active');
      }
    })
  }

  function deactiveAllAddressBoxes() {
    for (let item of addressBoxes) {
      item.classList.remove('active');
    }
  }

})();
