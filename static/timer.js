let targetTime = null;

// 获取后端当前倒计时目标
fetch("/get_time")
    .then(res => res.json())
    .then(data => {
        targetTime = new Date(data.target);
        startTimer();
    });

function startTimer() {
    setInterval(() => {
        if (!targetTime) return;

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
    }, 1000);
}

// 设置倒计时时长（分钟）
function updateTime() {
    const minutes = parseInt(document.getElementById("newTime").value);
    if (!minutes) return;
    
    fetch("/set_countdown", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({minutes: minutes})
    })
    .then(res => res.json().then(data => ({status: res.status, body: data})))
    .then(result => {
        if (result.status === 200) {
            targetTime = new Date(result.body.target);
            document.getElementById("msg").innerText = "";
        } else {
            document.getElementById("msg").innerText = result.body.msg;
        }
    });
}
