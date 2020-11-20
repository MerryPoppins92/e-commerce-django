$(document).ready(function(){
  // Contact form Handller
  var contactForm = $(".contact-form")
  var contactFormMethod = contactForm.attr("method")
  var contactFormEndpoint = contactForm.attr("action")
  
  function displaySubmit(submitBtn, defaultText, doSubmit){
    if (doSubmit) {
      submitBtn.addClass("disabled")
      submitBtn.html("<i class='fas fa-spinner'</i> Sending ...")
    } else {
      submitBtn.removeClass("disabled")
      submitBtn.html(defaultText)
    }
    
  }

  contactForm.submit(function(event){
    event.preventDefault()
    var contactFormSubmitBtn = contactForm.find("[type='submit']")
    var contactFormSubmitBtnTxt = contactFormSubmitBtn.text()
    var contactFormData = contactForm.serialize()
    var thisForm = $(this)
    displaySubmit(contactFormSubmitBtn, "", true)
    $.ajax({
      method: contactFormMethod,
      url: contactFormEndpoint,
      data: contactFormData,
      success: function(data){
        contactForm[0].reset()
        $.alert({
          title: "Success!!",
          content: "Thank you for your submission",
          theme: "modern"
        })
        setTimeout(function(){
          displaySubmit(contactFormSubmitBtn, contactFormSubmitBtnTxt, false)
        }, 2000)
      },
      error: function(error){
        console.log(error.responseJSON)
        var jsonData = error.responseJSON
        var msg = ""
        $.each(jsonData, function(key, value){
          msg += key + ": " + value[0].message + "<br/>"
        })
        $.alert({
          title: "Ooops!",
          content: msg,
          theme: "modern"
        })
        setTimeout(function(){
          displaySubmit(contactFormSubmitBtn, contactFormSubmitBtnTxt, false)
        }, 2000)
      }
    })
  })

  // Auto Search
  var searchForm = $(".search-form");
  var searchInput = searchForm.find("[name='q']")
  var typingTimer;
  var typingInterval = 500;
  var searchBtn = searchForm.find("[type='submit']")

  searchInput.keyup(function(event){
    clearTimeout(typingTimer)
    typingTimer = setTimeout(performSearch, typingInterval)
  })

  searchInput.keydown(function(event){
    clearTimeout(typingTimer)
  })

  function displaySearch(){
    searchBtn.addClass("disabled")
    searchBtn.html("<i class='fas fa-spinner'</i> Searching ...")
  }

  function performSearch(){
    displaySearch()
    var query = searchInput.val()
    setTimeout(function(){
      window.location.href='/search/?q=' + query
    }, 1000)
  }


  // Cart + Add Product
  var productForm = $(".form-product-ajax")
  productForm.submit(function(event){
    event.preventDefault();
    // console.log("form is not sending")
    var thisForm = $(this)
    // var actionEndpoint = thisForm.attr("action");
    var actionEndpoint = thisForm.attr("data-endpoint");
    var httpMethod = thisForm.attr("method");
    var formData = thisForm.serialize();

    
    $.ajax({
      url: actionEndpoint,
      method: httpMethod,
      data: formData,
      success: function(data){
        var submitSpan = thisForm.find(".submit-span");
        if (data.added) {
          submitSpan.html("In Cart <button type='submit' class='btn btn-link'>Remove?</button>")
        } else {
          submitSpan.html("<button class='btn btn-success'>Add to Cart?</button>")
        }

        var navbarCount = $(".navbar-cart-count")
        navbarCount.text(data.cartItemCount)

        var currentPath = window.location.href
        if (currentPath.indexOf("cart") != -1) {
          refreshCart()
        }
      },
      error: function(errorData){
        $.alert({
          title: "Ooops!",
          content: "An error occured",
          theme: "modern"
        })
      }
    })
  })
  function refreshCart(){
    console.log("in current cart")
    var cartTable = $(".cart-table");
    var cartBody = cartTable.find(".cart-body");
    // cartBody.html("<h1>Changed</h1>")
    var productRows = cartBody.find(".cart-products");
    var currentUrl = window.location.href

    var refreshCartUrl = '/api/cart';
    var refreshCartMethod = "GET";
    var data = {};

    $.ajax({
      url: refreshCartUrl,
      method: refreshCartMethod,
      data: data,
      success: function(data){
        console.log("success")
        console.log(data)
        if (data.length > 0) {
          productRows.html("<tr><td colspan=3>Coming Soon</td></tr>")
          cartBody.find(".cart-total").text(data.total)
        } else {
          window.location.href = currentUrl
        }
      },
      error: function(errorData){
        $.alert({
          title: "Ooops!",
          content: "An error occured",
          theme: "modern"
        })
      }
    })
  }

})
