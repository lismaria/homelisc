$(document).ready(function () {

    //Storing the initial height of the inner window
    let init_vh = window.innerHeight * 0.01;

    // For bottom nav bar in almost every mobile device
    window.addEventListener('resize', () => {
        // First we get the viewport height and we multiple it by 1% to get a value for a vh unit
        let vh = window.innerHeight * 0.01;
        // Then we set the value in the --vh custom property to the root of the document
        document.documentElement.style.setProperty('--vh', `${vh}px`);
    });

    $("#vendor_profile").click(() => {
        $(".vendor-acc-profile").slideToggle("slow");
    })

});
