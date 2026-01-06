((()=>{
    let imageAr = [
        'static/images/Cantor.png', 
        'static/images/Cantor2.png',
        'static/images/Cantor3.png'
      ];
    document.getElementById('myImages').setAttribute('src', imageAr[currentIndex = 0]);
    function chgImage() {
        currentIndex++;
        if (currentIndex >= imageAr.length) {
            currentIndex = 0;
          }
        document.getElementById('myImages').setAttribute('src', imageAr[currentIndex]);

      }
let intervalId = setInterval(chgImage, 3000);
  document.getElementById('myImages').addEventListener('click', chgImage);
}
))()
