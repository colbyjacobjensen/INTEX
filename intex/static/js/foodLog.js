var table  = document.getElementById('foodtable');
var calories = 0, fat = 0, carbohydrates = 0, protein = 0 ;

for(var i = 1; i <table.rows.length - 1; i++) {
    calories += parseFloat(table.rows[i].cells[1].innerHTML);

    fat += parseFloat(table.rows[i].cells[2].innerHTML);
    fat = Math.round(fat);

    carbohydrates += parseFloat(table.rows[i].cells[3].innerHTML);
    carbohydrates = Math.round(carbohydrates);

    protein += parseFloat(table.rows[i].cells[4].innerHTML);
    protein = Math.round(protein);    
}

document.getElementById('totalCalories').innerHTML = '<b>' + calories + '</b>';
document.getElementById('totalFat').innerHTML = '<b>' + fat + '</b>';
document.getElementById('totalCarbohydrates').innerHTML = '<b>' + carbohydrates + '</b>';
document.getElementById('totalProtein').innerHTML = '<b>' + protein + '</b>';

var total = fat + carbohydrates + protein;

var fatPercentage =  Math.round((fat / total) * 100);
var carbohydratesPercentage =  Math.round((carbohydrates / total) * 100);
var proteinPercentage =  Math.round((protein / total) * 100);

fatPercentage = fatPercentage ? fatPercentage : 0;
carbohydratesPercentage = carbohydratesPercentage ? carbohydratesPercentage : 0;
proteinPercentage = proteinPercentage ? proteinPercentage : 0;


// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", "Liberation Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"';
Chart.defaults.global.defaultFontColor = '#858796';

// Doughnut Chart - Macronutrients breakdown
var ctx = document.getElementById('myPieChart2');
var myPieChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: [
            'Fat ' + fatPercentage + '%', 
            'Carbs ' +  carbohydratesPercentage + '%', 
            'Protein ' + proteinPercentage + '%'
        ],
        datasets: 
        [
            {
                data: [fatPercentage, carbohydratesPercentage, proteinPercentage],
                backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc'],
                hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf'],
                hoverBorderColor: "rgba(234, 236, 244, 1)",
            }
        ],
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        animation: {
            animateScale: true,
        },
        plugins: {
            legend: {
                display: true,
                position: 'bottom',
            },
            title: {
                display: true,
                text: 'Macronutrients Breakdown',
                font: {
                    size: 20,
                },
            },
            datalabels: {
                display: true,
                color: '#fff',
                font: {
                    weight: 'bold',
                    size: 16,
                },
                textAlign: 'center',
            },
        },
    },
});


// options: {
//     maintainAspectRatio: false,
//     tooltips: {
//       backgroundColor: "rgb(255,255,255)",
//       bodyFontColor: "#858796",
//       borderColor: '#dddfeb',
//       borderWidth: 1,
//       xPadding: 15,
//       yPadding: 15,
//       displayColors: false,
//       caretPadding: 10,
//     },
//     legend: {
//       display: false
//     },
//     cutoutPercentage: 80,
//   },


// Calorie Goal Progress Bar

var caloriePercentage = (calories / 2000) *  100;
//document.getElementById('progressBar').setAttribute('style', 'width:' + caloriePercentage + '%');

$('.progress-bar').animate({
    width: caloriePercentage + '%',

}, 500);
var interval = setInterval(function () {
$('.progress-bar').html(caloriePercentage + '%');

}, 500);