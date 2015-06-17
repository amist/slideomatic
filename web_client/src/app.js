var myApp = angular.module('myApp', [])
myApp.controller('myController', function($scope) {
    var slide =  function(){
            this.content = ''}

    $scope.title = ""

    $scope.author = ""

    $scope.backend = ""

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
         for (s in $scope.slides) {
             paragraphs.push(s.content)
         }

        $.post(
            "slides_data",
            JSON.stringify(
                {"tile": $scope.title, "author": $scope.author,
                "paragraphs" : paragraphs, "backend": $scope.slides}),
            function (ret_data, st) {
                $.each(ret_data, function (index, value) {
                    alert("index: " + index + " , value: " + value);
                });
                alert("Server return status : " + st);
            },
            'json'
        );
    }



    }   )
