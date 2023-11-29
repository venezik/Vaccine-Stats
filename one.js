"use strict"
function ajaxGetRequest(path, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("GET", path);
    request.send();
}

function ajaxPostRequest(path, data, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("POST", path);
    request.send(data);
}
function getData(){
    ajaxGetRequest("/bar", showBar); 
    ajaxGetRequest("/pie",showPie)
}

function showBar(response) {
    // Data is always sent in JSON, so we must first convert it
    let data = JSON.parse(response);
    let layout = {
        title: "Fully Vaccinated by Location", 
        yaxis: {"title": "% Fully Vaccinated"},
        marker: {color: 'red'},
        xaxis: {"title": "Location"},
        plot_bgcolor: "transparent",
        paper_bgcolor: "transparent",
    }

    Plotly.newPlot("bar", data, layout);
}

function showPie(response){
    let data = JSON.parse(response);
    let layout = {
        title: "Vaccine Manufacturer Market Share",
        plot_bgcolor: "transparent",
        paper_bgcolor: "transparent",
    }
    Plotly.newPlot("pie", data, layout);
}

function getLocData(){
    let div = document.getElementById("locText")
    let data = div["value"]
    let locBlob = JSON.stringify(data);
    ajaxPostRequest("/line", locBlob, showLine);
}

function showLine(response){
    let data = JSON.parse(response);
    let layout = {
        title: "Fully Vaccinated by Location", 
        yaxis: {"title": "% Fully Vaccinated"}, 
        xaxis: {"title": "Date"},
        plot_bgcolor: "transparent",
        paper_bgcolor: "transparent",
    }
    Plotly.newPlot("line", data, layout);
}