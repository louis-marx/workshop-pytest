from calculate.controller import Controller


def test_addition(mocker):
    expected_value = 1.0
    controller = Controller()
    mock = mocker.patch("calculate.view.View.get_user_input")
    mock.side_effect = ["1", "10+10", "5"]
    mocker.patch("calculate.operators.Operators.addition", return_value=expected_value)
    mocker.patch("calculate.view.View.continue_message")

    controller.run()
    assert controller.result == expected_value
