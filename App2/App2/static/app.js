// static/app.js
document.addEventListener("DOMContentLoaded", () => {
    function fetchWeatherSummary() {
        fetch('/weather_summary')
            .then(response => response.json())
            .then(data => {
                document.getElementById('weatherSummary').innerText = JSON.stringify(data);
            });

        fetch('/alerts')
            .then(response => response.json())
            .then(data => {
                document.getElementById('alerts').innerText = data.message;
            });
    }

    setInterval(fetchWeatherSummary, 300000); // Refresh every 5 minutes
});
