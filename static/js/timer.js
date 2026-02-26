let targetTime = null;
let totalDuration = null;

// 页面加载时获取当前倒计时目标
fetch("/get_time")
    .then(res => res.json())
    .then(data => {
        if (data.target) {
            targetTime = new Date(data.target);
            totalDuration = targetTime - new Date();
        }
        startTimer();
    });



function startTimer() {
    setInterval(() => {
        if (!targetTime) {
            document.getElementById("timer").innerText = "未开始倒计时";
            return;
        }

        const now = new Date();
        const diff = targetTime - now;

        if (diff <= 0) {
            document.getElementById("timer").innerText = "时间到了";
            return;
        }

        const minutes = Math.floor(diff / (1000 * 60));
        const seconds = Math.floor(diff / 1000) % 60;

        document.getElementById("timer").innerText =
            `${minutes} 分 ${seconds} 秒`;
        updateCar(diff, totalDuration);

    }, 1000);
    
}

// 设置倒计时时长（分钟）
function setCountdown() {
    const minutes = parseInt(document.getElementById("minutes").value);
    if (!minutes) return;

    fetch("/set_countdown", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ minutes: minutes })
    })
        .then(res => res.json().then(data => ({ status: res.status, body: data })))
        .then(result => {
            if (result.status === 200) {
                targetTime = new Date(result.body.target);
                totalDuration = minutes * 60 * 1000;
                document.getElementById("msg").innerText = "";
            } else {
                document.getElementById("msg").innerText = result.body.msg;
            }
        });
}


const car = document.querySelector(".car");
const road = document.querySelector(".road");

function updateCar(diff, totalDuration) {
    if (!car || !road) return;

    const roadWidth = road.offsetWidth - car.offsetWidth;

    if (diff <= 0) {
        car.style.transform = `translateX(${roadWidth}px)`;
        return;
    }

    const progress = 1 - diff / totalDuration;
    car.style.transform = `translateX(${roadWidth * progress}px)`;
}