from trackr.main import parse_arguments


class TestParser:

    def test_test(self): 
        args = parse_arguments(['test', 'config/path/notify.yaml'])
        assert args.command == 'test'
        assert args.notify == 'config/path/notify.yaml'
