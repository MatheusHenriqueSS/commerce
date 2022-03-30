if (window.history.replaceState) {
    window.history.replaceState( null, null, window.location.href );
}

$("#bidding_val").keydown(function(evt) {
    if ((evt.which < 48 || evt.which > 57) && evt.which!= 13 && evt.which != 8 && evt.which != 46 && !(evt.which >= 37 && evt.which <= 40)
    && !(evt.which >= 96 && evt.which <= 105)) {
          evt.preventDefault();
    }
    var old_money = $("#bidding_val").val();
    var cursor_position = evt.target.selectionStart;
    var len = old_money.length;

    if(evt.which == 8 && cursor_position > 0 && (old_money[cursor_position - 1] == "." || old_money[cursor_position - 1] == ",") 
    && cursor_position == evt.target.selectionEnd) 
    {
        evt.preventDefault();
        if (cursor_position > 1) {
            let tmp1 = old_money.substr(0, cursor_position - 2);
            let tmp2 = old_money.substr(cursor_position);
            $("#bidding_val").val(tmp1 + tmp2);
            $("#bidding_val").css("width", $("#bidding_val").val().length + "ch");
        }    
    }
    if(evt.which == 46 && cursor_position < len - 1 && (old_money[cursor_position] == "." || old_money[cursor_position] == ",") 
    && cursor_position == evt.target.selectionEnd) 
    {
        evt.preventDefault();

        if (cursor_position < len - 2) {
            let tmp1 = old_money.substr(0, cursor_position + 1);
            let tmp2 = old_money.substr(cursor_position + 2);
            $("#bidding_val").val(tmp1 + tmp2);
            $("#bidding_val").css("width", $("#bidding_val").val().length + "ch");
        }    
    }
    setTimeout(function() {
    var money = $("#bidding_val").val();    

    money = money.replaceAll(',', '');
    money = money.replaceAll('.', '');
    let index = -1;
    for (let i = 0; i < money.length; i++) {
        if (money[i] != 0) break;
        index++;
    }
    if (index >= 0) {
        money = money.substr(index + 1);
    }
    if (money.length < 3) {
        money = "0".repeat(3 - money.length) + money;
    }
    let pt1 = money.substr(0, money.length - 2);
    let pt2 = money.substr(money.length - 2);
    let tmp = "";
    if (pt1.length > 3) {
        for (let i = pt1.length - 1; i >= 0; i--){
            tmp += pt1[i];
            if ((Math.abs(i - pt1.length + 1)) % 3 == 2 && i > 0)tmp += ",";
        }
        pt1 = tmp.split("").reverse().join("");
    }   
    $("#bidding_val").val(pt1 + "." + pt2);   
    $("#bidding_val").css("width", $("#bidding_val").val().length + "ch");
    }, 0);

});


$("#bidding-form").submit(function(evt) {
    var current_val = parseInt($("#current_value").text().replaceAll('$', '').replaceAll('.','').replaceAll(',',''))/100;
    current_val = current_val.toFixed(2);

    var bidding_val = parseInt($("#bidding_val").val().replaceAll('$','').replaceAll('.','').replaceAll(',',''))/100;
    bidding_val = bidding_val.toFixed(2);
    
    evt.preventDefault();
    if (parseFloat(bidding_val) <= parseFloat(current_val)) {        
        alert("The bidding value must be greater than the current value: $" + current_val)
    }
    else {
        var catid = $("#bidding_value").attr("value");
        console.log(catid + bidding_val);
        $.ajax(
            {
                type: "POST",
                url: "http://127.0.0.1:8000/bid",
                data: {
                    product_id: catid,
                    bidding_val: bidding_val
                },
                success : function(data)
                {
                    data = data.replace(/\B(?=(\d{3})+(?!\d))/g, ",");
                    $("#current_value").text("$" + data);
                }
            }
        )
    }
    $("#bidding_val").val("$0.00");
    $("#bidding_val").css("width", $("#bidding_val").val().length + "ch");
});

$(".heart-like-button").each(function () {
    var button = $(this);
    var catid;
    catid = $(this).attr("data-catid");
    $.ajax(
        {
            type: "POST",
            url: "http://127.0.0.1:8000/on_watchlist",
            data: {
                product_id: catid
            },
            success : function(data)
            {
                if (data == "1") {
                    button.addClass("liked");
                }
                else {
                    button.removeClass("liked");
                }
            }
        }
    )
});

$(".heart-like-button").click(function(){    
    var button = $(this);
    var catid;
    catid = $(this).attr("data-catid"); 
    console.log(catid); 
    $.ajax(
        {
            type: "POST",
            url: "http://127.0.0.1:8000/watchlist",
            data: {
                auction_id: catid
            },
            success: function()
            {
                button.toggleClass("liked");
            }
        }
    )
});



//navbar dropdown menu

// $("#dropdownMenuButton").click(function() {
//     $(".dropdown-menu").toggleClass("show");
// });

// window.click(function(evt) {
//     if (!evt.target.matches('#dropdownMenuButton')) {
//         $(".dropdown-menu").removeClass("show");
//     }
// });


//$(".dropdown-toggle").dropdown("show");


$(".card-body h4").each(function(index) {
    let title = $(this).text();
    if (title.length > 42) {
        title = title.substr(0, 39);
        title += "..."
    }

    $(this).text(title)
});


$(".card-text").each(function(index) {
    let text = $(this).text();

    if (text.length > 180) {
        text = text.substr(0, 177);
        text += "...";
    }

    $(this).text(text);
});


$(".card").click(function(index) {
    let link = $(this).find('a').attr('href');
    location.href = link;
});

$("#searchBox").keyup(function(evt) {
    var search = $("#searchBox").val().toLowerCase();
    search = search.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
       
    $(".col-md-6.col-lg-4").each(function(index) {
        var productName = $(this).find('.card-body div').data("title").toLowerCase();
        productName = productName.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
        console.log(search, productName);
        
        if (search == "" || productName.includes(search)) {
            $(this).removeClass("d-none");
        }
        else {
            $(this).addClass("d-none");
        }
        
    })
    $(".category").each(function(index) {
        var productName = $(this).text().toLowerCase();
        productName = productName.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
        console.log(search, productName);
        
        if (search == "" || productName.includes(search)) {
            $(this).parent().parent().removeClass("d-none");
        }
        else {
            $(this).parent().parent().addClass("d-none");
        }
        
    })
});

//set scrollbar to the end of commentary section
$("#commentBox").scrollTop($("#commentBox")[0].scrollHeight);



