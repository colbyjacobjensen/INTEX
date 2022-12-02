var table  = document.getElementById('foodtable');
var calories = 0, fat = 0, carbohydrates = 0, protein = 0, potassium = 0, sodium = 0;

for(var i = 1; i <table.rows.length - 1; i++) {
    calories += parseFloat(table.rows[i].cells[1].innerHTML);

    fat += parseFloat(table.rows[i].cells[2].innerHTML);
    fat = Math.round(fat);

    carbohydrates += parseFloat(table.rows[i].cells[3].innerHTML);
    carbohydrates = Math.round(carbohydrates);

    protein += parseFloat(table.rows[i].cells[4].innerHTML);
    protein = Math.round(protein);
    
    potassium += parseFloat(table.rows[i].cells[5].innerHTML);
    potassium = Math.round(potassium);

    sodium += parseFloat(table.rows[i].cells[6].innerHTML);
    sodium = Math.round(sodium);

}

document.getElementById('totalCalories').innerHTML = '<b>' + calories + '</b>';
// document.getElementById('totalFat').innerHTML = '<b>' + fat + '</b>';
// document.getElementById('totalCarbohydrates').innerHTML = '<b>' + carbohydrates + '</b>';
document.getElementById('totalProtein').innerHTML = '<b>' + protein + '</b>';
// document.getElementById('totalCalcium').innerHTML = '<b>' + calcium + '</b>';
document.getElementById('totalPotassium').innerHTML = '<b>' + potassium + '</b>';
// document.getElementById('totalPhosphorus').innerHTML = '<b>' + phosphorus + '</b>';
document.getElementById('totalSodium').innerHTML = '<b>' + sodium + '</b>';

// var total = fat + carbohydrates + protein;
var total = fat + carbohydrates + protein;

var fatPercentage =  Math.round((fat / total) * 100);
var carbohydratesPercentage =  Math.round((carbohydrates / total) * 100);
var proteinPercentage =  Math.round((protein / total) * 100);

// var calciumPercentage =  Math.round((calcium / total) * 100);
// var potassiumPercentage =  Math.round((potassium / total) * 100);
// var phosphorusPercentage =  Math.round((phosphorus / total) * 100);
// var sodiumPercentage =  Math.round((sodium / total) * 100);

fatPercentage = fatPercentage ? fatPercentage : 0;
carbohydratesPercentage = carbohydratesPercentage ? carbohydratesPercentage : 0;
proteinPercentage = proteinPercentage ? proteinPercentage : 0;

// calciumPercentage = calciumPercentage ? calciumPercentage : 0;
// potassiumPercentage = potassiumPercentage ? potassiumPercentage : 0;
// phosphorusPercentage = phosphorusPercentage ? phosphorusPercentage : 0;
// sodiumPercentage = sodiumPercentage ? sodiumPercentage : 0;


// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", "Liberation Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"';
Chart.defaults.global.defaultFontColor = '#858796';
  
// if potassiumGoalNum > 100:
//     messages.success(request, ("You have exceeded your potassium recommendation for the day! Limit your potassium intake for the rest of the day."))
// if sodiumGoalNum > 100:
//     messages.success(request, ("You have exceeded your sodium recommendation for the day! Limit your sodium intake for the rest of the day."))
// if sugarGoalNum > 100:
//     messages.success(request, ("You have exceeded your sugar recommendation for the day! Limit your sugar intake for the rest of the day."))
// if proteinGoalNum > 100:
//     messages.success(request, ("You have exceeded your protein recommendation for the day! Limit your protein intake for the rest of the day."))
// if fatGoalNum > 100:
//     messages.success(request, ("You have exceeded your fats recommendation for the day! Limit your fats intake for the rest of the day."))
// if carbGoalNum > 100:
//     messages.success(request, ("You have exceeded your carbohydrate recommendation for the day! Limit your carbohydrate intake for the rest of the day."))
// if calorieGoalNum > 100:
//     messages.success(request, ("You have exceeded your calorie recommendation for the day! Limit your calorie intake for the rest of the day."))
// if phosphorusGoalNum > 100:
//     messages.success(request, ("You have exceeded your phosphorus recommendation for the day! Limit your phosphorus intake for the rest of the day."))
// if calciumGoalNum > 100:
//     messages.success(request, ("You have exceeded your calcium recommendation for the day! Limit your calcium intake for the rest of the day."))



// Doughnut Chart - Macronutrients breakdown
var ctx = document.getElementById('myPieChart2');
var myPieChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: [
            'Fat ' + fatPercentage + '%', 
            'Carbohydrates ' + carbohydratesPercentage + '%',
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

// var caloriePercentage = round(((calories / 2000) *  100),2);
var caloriePercentage = (calories / 2000) *  100;
caloriePercentage = Math.floor(caloriePercentage);
// document.getElementById('progressBar').setAttribute('style', 'width:' + caloriePercentage + '%');

$('.progress-bar').animate({
    width: caloriePercentage + '%',

}, 500);
var interval = setInterval(function () {
$('.progress-bar').html(caloriePercentage + '%');

}, 500);