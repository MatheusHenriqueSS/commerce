var counter = 0;
(function priceUpdate() {
    var catid = $(".listing-title").attr("data-catid");
    console.log("debug:" + catid);
    if($("#close").hasClass("overlay")){
        return
    }
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/is_active",
        data: {
            product_id: catid
        },
        success: function(data)
        {   
            if (data == "0") {
                location.reload();
            }
        }
    });
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/current_price",
        data: {
            product_id: catid
        },
        success: function(data)
        {
            data = data.replace(/\B(?=(\d{3})+(?!\d))/g, ",");
            $("#current_value").text("$" + data);
        }
    });
    setTimeout(priceUpdate, 5000);
})();