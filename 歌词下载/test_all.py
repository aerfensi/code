import unittest
import lyric_crawler
import funcs


class TestLyricCrawler(unittest.TestCase):

    @unittest.skip
    def test_user_in(self):
        try:
            args = lyric_crawler.user_in()
            self.assertEqual(3, len(args))
            self.assertTrue(isinstance(args[0], str) and args[0].isdigit())
            self.assertIsInstance(args[1], lyric_crawler.SOURCE)
            self.assertIsInstance(args[2], str)
        except BaseException as e:
            self.assertIsInstance(e, SystemExit)

    @unittest.skip
    def test_merge_lrc(self):
        try:
            funcs.merge_lrc(None, None)
        except BaseException as e:
            self.assertIsInstance(e, AssertionError)

    @unittest.skip
    def test_fetch_qq(self):
        lrc = lyric_crawler.Lyric('002BUvdb0Pw3q3', lyric_crawler.SOURCE.Tencent, 'None')
        response = lrc.fetch(funcs.fetch_qq).response
        self.assertEqual(response.status_code, 200)
        self.assertRegex(response.text, '^MusicJsonCallback_lrc')

    def test_extract_qq(self):
        respone = type('Respone', (), {})
        respone.status_code = 200
        respone.text = ('MusicJsonCallback_lrc({'
                        '"retcode":0,'
                        '"code":0,'
                        '"subcode":0,'
                        '"lyric":"W3RpOuivpeatu+eahOa4qeaflF0KW2FyOueOi+mbhea0gV0KW2FsOjIyOTc3M10KW2J5Ol0KW29mZnNldDowXQpbMDA6MDAuMDBd6K+l5q2755qE5rip5p+UIC0g546L6ZuF5rSBIChOaWNvbGUgV2FuZykKWzAwOjQ2LjI2XeivtOWlveS7juatpOWQjgpbMDA6NDguOTJdClswMDo0OS42Nl3or7Tlpb3ms6rkuI3mtYEKWzAwOjUyLjQ2XQpbMDA6NTMuMDVd57yY5Lu95bey5bC955qE5pe25YCZClswMDo1Ni40OF3kvaDkuI3lho3opoHlgJ/lj6MKWzAwOjU5LjUxXemjjuWBnOS6hgpbMDE6MDEuMzBd6Zuo6aG/5LqGClswMTowMy40MV3kvaDkuIDlrpropoHotbAKWzAxOjA2LjQ4XeaIkei/mOermeWcqOiusOW/humHjApbMDE6MDkuNDJd5Zyo5oSf5Y+XClswMToxMy4zMF3kvaDov5nor6XmrbvnmoTmuKnmn5QKWzAxOjE2LjY0XeiuqeaIkeW/g+WcqOeXm+azquWcqOa1gQpbMDE6MjAuMTRd5bCx5Zyo5ZKM5L2g6K+05YiG5omL5Lul5ZCOClswMToyMy41N13mg7Plv5jorrDlt7LkuI3og73lpJ8KWzAxOjI2Ljk5XeS9oOi/meivpeatu+eahOa4qeaflApbMDE6MzAuNDVd6K6p5oiR5q2i5LiN5L2P6aKk5oqWClswMTozMy45MF3lk6rmgJXmnInlho3lpJrnmoTlgJ/lj6MKWzAxOjM3LjQ1XeaIkemDveaXoOazleWGjeWOu+eJteS9oOeahOaJiwpbMDE6NDQuMTldClswMTo1NC44NV3or7Tlpb3ku47mraTlkI4KWzAxOjU3LjcxXQpbMDE6NTguMjRd6K+05aW95rOq5LiN5rWBClswMjowMS4xN10KWzAyOjAxLjY5Xee8mOS7veW3suWwveeahOaXtuWAmQpbMDI6MDUuMDhd5L2g5LiN5YaN6KaB5YCf5Y+jClswMjowOC4yMl3po47lgZzkuoYKWzAyOjA5Ljg5XembqOmhv+S6hgpbMDI6MTIuMDJd5L2g5LiA5a6a6KaB6LWwClswMjoxNS4wN13miJHov5jnq5nlnKjorrDlv4bph4wKWzAyOjE3Ljk3XeWcqOaEn+WPlwpbMDI6MjEuOTRd5L2g6L+Z6K+l5q2755qE5rip5p+UClswMjoyNS4zMV3orqnmiJHlv4PlnKjnl5vms6rlnKjmtYEKWzAyOjI4Ljc5XeWwseWcqOWSjOS9oOivtOWIhuaJi+S7peWQjgpbMDI6MzIuMzld5oOz5b+Y6K6w5bey5LiN6IO95aSfClswMjozNS43MF3kvaDov5nor6XmrbvnmoTmuKnmn5QKWzAyOjM5LjE3XeiuqeaIkeatouS4jeS9j+mipOaKlgpbMDI6NDIuNThd5ZOq5oCV5pyJ5YaN5aSa55qE5YCf5Y+jClswMjo0Ni4zM13miJHpg73ml6Dms5Xlho3ljrvnibXkvaDnmoTmiYsKWzAyOjUyLjk1XeS9oOi/meivpeatu+eahOa4qeaflApbMDI6NTYuMzNd6K6p5oiR5b+D5Zyo55eb5rOq5Zyo5rWBClswMjo1OS44MV3lsLHlnKjlkozkvaDor7TliIbmiYvku6XlkI4KWzAzOjAzLjIyXeaDs+W/mOiusOW3suS4jeiDveWknwpbMDM6MDYuNjRd5L2g6L+Z6K+l5q2755qE5rip5p+UClswMzoxMC4wOV3orqnmiJHmraLkuI3kvY/poqTmipYKWzAzOjEzLjUzXeWTquaAleacieWGjeWkmueahOWAn+WPowpbMDM6MTcuMTZd5oiR6YO95peg5rOV5YaN5Y6754m15L2g55qE5omLClswMzoyNC4yMF3lk6YgIApbMDM6MjYuOThd5ZOmICAKWzAzOjMwLjIwXeeJteS9oOeahOaJiwpbMDM6MzMuNjldClswMzozNS4xOF3nibXkvaDnmoTmiYs=",'
                        '"trans":""})')
        o_lrc, t_lrc = funcs.extract_qq(respone)
        # print('o_lrc = ', o_lrc, 't_lrc = ', t_lrc, sep='\n')
        self.assertNotEqual(o_lrc, None)


if __name__ == "__main__":
    unittest.main()
