
//1. 공부시간 측정 타이머
let timerId;
let time = 0;
const stopwatch = document.getElementById("stopwatch");
let  hour, min, sec;


function printTime() {
    time++;
    stopwatch.innerText = getTimeFormatString();
}

//시계 시작 - 재귀호출로 반복실행
function startClock() {
    printTime();
    stopClock();
    timerId = setTimeout(startClock, 1000);
}





//chart.js 폰트변경
Chart.defaults.global.defaultFontFamily = 'Noto Sans KR', 'sans-serif';
