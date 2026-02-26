const themeSelect = document.getElementById("themeSelect");

// 页面加载时读取主题
const savedTheme = localStorage.getItem("theme");
if (savedTheme) {
    themeSelect.value = savedTheme;
    applyTheme(savedTheme);
}

themeSelect.addEventListener("change", function() {
    const theme = this.value;
    localStorage.setItem("theme", theme);
    applyTheme(theme);
});

function applyTheme(theme) {
    switch(theme) {
        case "blue":
            document.documentElement.style.setProperty("--theme-topbg", "#e0e0ff");
            document.documentElement.style.setProperty("--theme-bottomleftbg", "#e0f0ff");
            document.documentElement.style.setProperty("--theme-bottomrightbg", "#f0e0ff" );
            document.documentElement.style.setProperty("--theme-card-bg", "#ffffff");
            document.documentElement.style.setProperty("--theme-card-top", "linear-gradient(135deg, #0a1a3f, #0f2a6b)");
            document.documentElement.style.setProperty("--theme-text", "#1e293b");
            document.documentElement.style.setProperty("--theme-button-bg", "#1e40af");
            document.documentElement.style.setProperty("--theme-button-text", "#ffffff");
            document.documentElement.style.setProperty("--theme-input-bg", "#ffffff");
            document.documentElement.style.setProperty("--theme-input-border", "#94a3b8");
            break;

        case "pink":
            document.documentElement.style.setProperty("--theme-topbg", "#ffe0e0");
            document.documentElement.style.setProperty("--theme-bottomleftbg", "#fff0e0");
            document.documentElement.style.setProperty("--theme-bottomrightbg", "#ffe0f0");
            document.documentElement.style.setProperty("--theme-card-bg", "#ffffff");
            document.documentElement.style.setProperty("--theme-card-top", "linear-gradient(135deg, #f48fb1, #f06292)");
            document.documentElement.style.setProperty("--theme-text", "#4a4a4a");
            document.documentElement.style.setProperty("--theme-button-bg", "#d81b60");
            document.documentElement.style.setProperty("--theme-button-text", "#ffffff");
            document.documentElement.style.setProperty("--theme-input-bg", "#ffffff");
            document.documentElement.style.setProperty("--theme-input-border", "#f48fb1");
            break;

        case "green":
            document.documentElement.style.setProperty("--theme-topbg", "#e0ffe0");
            document.documentElement.style.setProperty("--theme-bottomleftbg", "#f0ffe0");
            document.documentElement.style.setProperty("--theme-bottomrightbg", "#e0fff0");
            document.documentElement.style.setProperty("--theme-card-bg", "#ffffff");
            document.documentElement.style.setProperty("--theme-card-top", "linear-gradient(135deg, #1b5e20, #2e7d32)");
            document.documentElement.style.setProperty("--theme-text", "#2e2e2e");
            document.documentElement.style.setProperty("--theme-button-bg", "#2e7d32");
            document.documentElement.style.setProperty("--theme-button-text", "#ffffff");
            document.documentElement.style.setProperty("--theme-input-bg", "#ffffff");
            document.documentElement.style.setProperty("--theme-input-border", "#66bb6a");
            break;
    }
}
