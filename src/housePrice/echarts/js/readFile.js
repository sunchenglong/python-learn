/**
 * Created by sunchenglong on 17/3/13.
 */

function initAreaData() {
    var dataroot = "a.json";
    $.getJSON(dataroot, function (data) {
        areadata.date = data.date;
        areadata.region = data.region;
        areadata.price = data.price;
        areadata.pricePerA = data.pricePerA;
    });
}
initAreaData()