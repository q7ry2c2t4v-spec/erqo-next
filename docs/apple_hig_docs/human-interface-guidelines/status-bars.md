# ステータスバー

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/status-bars

# ステータスバー

ステータスバーは画面の上端にあり、時間、モバイル通信キャリア、バッテリー残量などのデバイスの現在の状態に関する情報を表示します。

![時間、モバイル通信、Wi-Fi、バッテリー残量を表示するラベルがある、図案化されたiPhoneのステータスバー。画像全体が、6色の初代Appleロゴの赤色を連想させる赤みを帯びています。](https://docs-assets.developer.apple.com/published/ab5c6b835682fa59583e7323394f5820/components-status-bar-intro%402x.png)

## [ベストプラクティス](/jp/design/human-interface-guidelines/status-bars#Best-practices)

**ステータスバーの下にあるコンテンツを隠す。** ステータスバーの背景はデフォルトでは透明なので、下のコンテンツが透けて見えます。このため、透過処理によってステータスバーに表示される情報が見にくくなることがあります。また、ステータスバーの後ろにコントロールが見えると、ユーザが操作しようとしても反応しないといったことが起きます。ステータスバーの情報を常に読み取りやすくすると共に、背後にあるコンテンツを操作できるかのような印象を与えないようにしましょう。ステータスバーの後ろにぼかしをかけたビューを配置するには、できるだけスクロールエッジエフェクトを使用してください。デベロッパ向けのガイダンスは、[`ScrollEdgeEffectStyle`](/documentation/SwiftUI/ScrollEdgeEffectStyle)および[`UIScrollEdgeEffect`](/documentation/UIKit/UIScrollEdgeEffect)を参照してください。

**メディアのフルスクリーン表示時にステータスバーを一時的に非表示にすることを検討する。** メディアに集中したいユーザにとってはステータスバーが邪魔になることがあります。イマーシブ感を高めるには、ステータスバーの要素を一時的に非表示にしましょう。例えば写真アプリでは、写真をフルスクリーンで表示しているときはステータスバーなどのインターフェイス要素が非表示になります。

![iPhoneの写真アプリの上半分のスクリーンショット。画面いっぱいに写真が表示されています。画面上部にステータスバーが表示されています。](https://docs-assets.developer.apple.com/published/253abd829c29ad1084b7196d9a279fdf/status-bar-visible%402x.png)

ステータスバーが表示されている写真アプリ

![iPhoneの写真アプリの上半分のスクリーンショット。画面いっぱいに写真が表示されています。ステータスバーは非表示で、写真のみが表示されています。](https://docs-assets.developer.apple.com/published/546831607b77b71bf7928e60e9949e9b/status-bar-hidden%402x.png)

ステータスバーが非表示の写真アプリ

**ステータスバーを常時非表示にすることは避ける。** ステータスバーがないと、時間やWi-Fi接続の有無を確認するのにわざわざアプリを離れなければならなくなります。簡単に見つけられるシンプルなジェスチャで非表示のステータスバーを再表示できるようにしてください。例えば写真アプリでは、写真をフルスクリーンで表示しているときでも1回タップするだけでステータスバーが再表示されます。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/status-bars#Platform-considerations)

 _iOS、iPadOSに追加の考慮事項はありません。macOS、tvOS、visionOS、watchOSには対応していません。_

## [リソース](/jp/design/human-interface-guidelines/status-bars#Resources)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/status-bars#Developer-documentation)

[`UIStatusBarStyle`](/documentation/UIKit/UIStatusBarStyle) — UIKit

[`preferredStatusBarStyle`](/documentation/UIKit/UIViewController/preferredStatusBarStyle) — UIKit
