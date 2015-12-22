Feature: Dummy scenario
    As a QA engineer
    I want to be able to test JSON placeholder API
    So that I can build up this test repo


    @demo
    Scenario: First example
        Given the SUT is available
        When I request to get all posts
        Then I should get a list of "100" posts


    @comments
    Scenario: Get comments
        Given the SUT is available
        When I request to get all comments
        Then I should get a list of "500" comments


    @albums
    Scenario: Get albums
        Given the SUT is available
        When I request to get all albums
        Then I should get a list of "100" albums


    @photos
        Scenario: Get photos
        Given the SUT is available
        When I request to get all photos
        Then I should get a list of "5000" photos


    @todos
        Scenario: Get todos
        Given the SUT is available
        When I request to get all todos
        Then I should get a list of "200" todos


    @users
        Scenario: Get users
        Given the SUT is available
        When I request to get all users
        Then I should get a list of "10" users




