(function () {
  'use strict';

  ymaps.ready(init);
  var myMap;
  var myPlacemark;

  function init() {
    myMap = new ymaps.Map("map", {
      center: [48.48230916240944, 135.07202358758627], // Координаты центра карты
      zoom: 15 // Маштаб карты
    });
    myMap.controls.add(
        new ymaps.control.ZoomControl()  // Добавление элемента управления картой
    );
    myMap.controls
        .remove('trafficControl') // Удаление элемента управления картой
        .remove('typeSelector')
        .remove('scaleLine')
        .remove('smallZoomControl')
        .remove('zoomControl')
        .remove('searchControl')
        .remove('mapTools');
    myPlacemark = new ymaps.Placemark(
        [48.48230916240944, 135.07202358758627], // Координаты метки объекта
        {balloonContentBody: 'ВелоСам'}, // Подсказка метки
        {preset: 'islands#blueBicycleIcon'} // Тип метки
    );
    myMap.geoObjects.add(myPlacemark); // Добавление метки
    // myPlacemark.balloon.open(); // Открытие подсказки метки
  };

})();