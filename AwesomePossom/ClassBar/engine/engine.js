let isMenuShown = true;

function hideMenu()
{
    if (isMenuShown == true)
    {
        $('.menu').slideUp();
        isMenuShown = false;
    }
}

function showMenu()
{
    if (isMenuShown == false)
    {
        $('.menu').slideDown();
        isMenuShown = true;
    }
}

function changeMenu()
{
    if (isMenuShown)
    {
        hideMenu();
    }
    else
    {
        showMenu();
    }
}

function startTimer()
{
    isOn = false;

    let timerVal = $('#time').val();
    if (timerVal == '')
    {
        timerVal = 50;
    }

    time = timerVal;
    getFramesTime();

    dino.reset();
    cactus.reset();

    hideMenu();
    isOn = true;
}