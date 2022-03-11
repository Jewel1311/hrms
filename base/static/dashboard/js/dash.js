$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });
});


$(document).on('click','ul li', function () {
        $(this).addClass('active').siblings().removeClass('active');
    });
