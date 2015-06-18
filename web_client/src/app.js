var myApp = angular.module('myApp', [])
myApp.controller('myController', function($scope) {
    var slide =  function(){
            this.content = ''
    this.wiki=false}

    $scope.title = ""

    $scope.author = ""

    $scope.backend = "impress"

    $scope.slides = [new slide()]  ;

    $scope.add_slide = function(){

        $scope.slides.push(new slide())
        //$scope.$apply()
    }

    $scope.remove_slide = function(slide_index){

        $scope.slides.splice(slide_index, 1);
        //$scope.$apply()
    }

    $scope.apply = function() {
        var paragraphs = []
        var slides = $scope.slides
        for (index = 0; index < slides.length; ++index) {
             var content = ""
             if (slides[index].wiki == true) { content = "WIKI:"}
             content += slides[index].content
             paragraphs.push(content)
         }

        var slides =  {"title": $scope.title, "author": $scope.author,
                    "paragraphs" : paragraphs, "backend": $scope.backend}

        slides = JSON.stringify(slides)
        //alert ("request data "+ slides)
        $.ajax({
            url: '/slides_data',
            type: 'post',
            data: JSON.stringify(slides, null, '\t'),
            contentType: 'application/json;charset=UTF-8',

            success: function (data) {
                alert("success!!!!!");
                //window.open('file:///C:/hackit/slideomatic/slides.html#/step-1');
                //window.location.href=”login.jsp?backurl=”+window.location.href;gi

            }

        });


    }



    }   )
