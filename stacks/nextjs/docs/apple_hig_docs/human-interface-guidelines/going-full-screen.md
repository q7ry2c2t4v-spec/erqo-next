# フルスクリーンモード

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/going-full-screen

# フルスクリーンモード

iPhone、iPad、Macには、ユーザがウインドウを画面いっぱいに拡張できるフルスクリーンモードがあります。フルスクリーンモードでは、システムコントロールが非表示になるので、ほかに気を取られることのない環境になります。

![左上から右下に伸びる直線に、外向きの2つの矢印が配置されたスケッチ。拡大を示しています。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせるオレンジ色になっています。](https://docs-assets.developer.apple.com/published/edb1dc8fdbc26c6788464653a0b8fb3a/patterns-going-full-screen-intro%402x.png)

Apple TVとApple Watchでは、アプリやゲームがデフォルトで画面いっぱいに表示されるので、フルスクリーンモードはありません。Apple Vision Proでは、ウインドウを拡張してビューに占める広さを増やしたり、Digital Crownでパススルーを非表示にして体験のイマーシブ度を上げたりできるので、フルスクリーンモードはありません（ガイダンスは、[イマーシブ体験](/jp/design/human-interface-guidelines/immersive-experiences)を参照してください）。

## [ベストプラクティス](/jp/design/human-interface-guidelines/going-full-screen#Best-practices)

**フルスクリーンモードは作業内容に適している場合に対応する。** ユーザがフルスクリーンモードを使用したいと考えるのは、タスクやコンテンツに集中したい場合です。ユーザにゲームをプレイしてもらったり、ビデオや写真のスライドショーなどのメディアを表示してもらったり、集中して作業を行ってもらう場合は、フルスクリーンモードの提供を検討してください。

**必要な場合はフルスクリーンモードでレイアウトを調整するが、プログラムでウインドウのサイズを変更しない。** フルスクリーンモードのウインドウがフルスクリーンモードでないウインドウよりも大きくなる場合は、追加スペースを有効活用しながら、重要なコンテンツを目立たせるとよいでしょう。例えば、表示する項目を変更せずにインターフェイスの比率を調整すると、分かりやすい場合があります。このような調整を行う場合は、一貫したインターフェイスを維持し、モードが変わるときの画面遷移がぎこちなくならないように、細かな調整にとどめるようにしてください。

**フルスクリーンモードを維持したままユーザがタスクを完了できるように必須の機能やコントロールは常に利用可能にしておく。** 例えば、フルスクリーンのメディア体験では、再生コントロールを常時表示するか、ユーザの必要に応じてすぐに表示できるようにする必要があります。

**ゲームを除きiPadOSのアプリやmacOSのアプリがフルスクリーンモードになっている間でもユーザがDockを表示できるようにする。** iPadOSとmacOSでは、ユーザがほかのアプリやDock項目を素早く開けるように、いつでもDockを操作できるようにしておくことは重要です。フルスクリーンゲームをプレイしているときに意図せずDockが表示されることがないように、iPadOSで画面下端からの最初の上スワイプを無視したり、macOSでDockを完全に非表示にしたりするリクエストを行うことができます。デベロッパ向けのガイダンスは、[`preferredScreenEdgesDeferringSystemGestures`](/documentation/SwiftUI/UIHostingController/preferredScreenEdgesDeferringSystemGestures)（SwiftUI）、[`preferredScreenEdgesDeferringSystemGestures`](/documentation/UIKit/UIViewController/preferredScreenEdgesDeferringSystemGestures)（UIKit）、および[`hideDock`](/documentation/AppKit/NSApplication/PresentationOptions-swift.struct/hideDock)（AppKit）を参照してください。

**いったん離れたフルスクリーン体験にユーザが戻ってきたときには、離れたときの状態から再開できるようにする。** 例えばゲームやスライドショーでは、ユーザが体験から離れたら、見逃しが発生しないように自動的に一時停止する必要があります。

**ユーザがフルスクリーンモードを終了するタイミングを選べるようにする。** 別の体験に切り替えるときや、ゲームプレイやムービーの視聴などの没頭型のアクティビティを終えるときに、フルスクリーンモードが勝手に終了するのは、一般的にユーザの期待する動作ではありません。

**ツールバーやナビゲーションコントロールを一時的に非表示にして、コンテンツを優先させる。** フルスクリーンで写真を表示したり、書類を読んだりするなど、コンテンツに集中してもらう場合は、要素を非表示にして、ほかに気を取られない環境にすることができます。このような動作を実装する場合は、タップ、下にスワイプ、カーソルを画面の上部に移動するなど、使い慣れたジェスチャやアクションで非表示にした要素を復元できるようにしてください。ナビゲーションやタスクの実行に不可欠なコントロールは、必ず表示したままにしてください。visionOSのウインドウでもツールバーやナビゲーションコントロールを非表示にすることはできますが、Apple Vision Proを装着中のユーザは、それとは異なるタイプのイマーシブ体験を期待すると考えられます。ガイダンスは、[イマーシブ体験](/jp/design/human-interface-guidelines/immersive-experiences)を参照してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/going-full-screen#Platform-considerations)

 _tvOS、visionOS、watchOSには対応していません。_

### [iOS/iPadOS](/jp/design/human-interface-guidelines/going-full-screen#iOS-iPadOS)

**フルスクリーンのアプリやゲームで誤って終了してしまうことを防ぐため、システムジェスチャを遅らせることを検討する。** デフォルトでは、ホーム画面インジケータは、アプリやゲームに切り替えた直後に自動的に非表示になります。画面下部を操作すると再び表示され、1回スワイプすると終了することができます。これはユーザにとって馴染みがあり、期待される動作であるため、可能な限り維持してください。この動作に対応すると突然終了してしまう場合は、1回ではなく2回スワイプして終了させることもできます。デベロッパ向けのガイダンスは、[`preferredScreenEdgesDeferringSystemGestures`](/documentation/SwiftUI/UIHostingController/preferredScreenEdgesDeferringSystemGestures)を参照してください。

### [macOS](/jp/design/human-interface-guidelines/going-full-screen#macOS)

**システムが提供するフルスクリーン機能を使う。** システムのフルスクリーン機能を使うと、あらゆる状況でフルスクリーンウインドウの正常な動作が保証されます。例えば、Macには、画面の上部中央の領域がカメラハウジングで隠れる機種があります。システムのフルスクリーン対応を使うと、この領域への対応が自動的に行われます。デベロッパ向けのガイダンスは、[`toggleFullScreen(_:)`](/documentation/AppKit/NSWindow/toggleFullScreen\(_:\))を参照してください。

**ゲームでプレイヤーがフルスクリーンにした場合は、表示モードを変更しない。** ユーザは表示モードを操作できることを期待しており、自動的に表示モードを変更しても、パフォーマンスは向上しません。

デベロッパ向けの追加ガイダンスは、[macOSでMetal向けにゲームウインドウを管理する](/documentation/Metal/managing-your-game-window-for-metal-in-macos)（英語）を参照してください。

**常にユーザがフルスクリーンモードにするタイミングを選べるようにする。** ユーザがウインドウの「フルスクリーンにする」ボタン、「表示」メニュー項目、Control＋Command＋Fキーボードショートカットを使えるようにします。ウインドウモードのカスタムメニューを提供しないようにしてください。ゲームでは、フルスクリーンモードのオン/オフを切り替えるカスタムの[トグル](https://developer.apple.com/jp/design/human-interface-guidelines/toggles)を提供することもできます。

## [リソース](/jp/design/human-interface-guidelines/going-full-screen#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/going-full-screen#Related)

[レイアウト](/jp/design/human-interface-guidelines/layout)

[マルチタスク](/jp/design/human-interface-guidelines/multitasking)

[ウインドウ](/jp/design/human-interface-guidelines/windows)

[メニューバー](/jp/design/human-interface-guidelines/the-menu-bar)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/going-full-screen#Developer-documentation)

[`fullScreenCover(item:onDismiss:content:)`](/documentation/SwiftUI/View/fullScreenCover\(item:onDismiss:content:\)) — SwiftUI

[`NSScreen`](/documentation/AppKit/NSScreen) — AppKit

[`NSWindow.CollectionBehavior`](/documentation/AppKit/NSWindow/CollectionBehavior-swift.struct) — AppKit

[macOSでMetal向けにゲームウインドウを管理する](/documentation/Metal/managing-your-game-window-for-metal-in-macos)（英語） — Swift、Objective-C

#### [ビデオ](/jp/design/human-interface-guidelines/going-full-screen#Videos)

[](https://developer.apple.com/videos/play/wwdc2025/208)

## [変更履歴](/jp/design/human-interface-guidelines/going-full-screen#Change-log)

日付| 変更内容  
---|---  
2025年6月09日| ツールバーとナビゲーションコントロールを非表示にするためのガイダンス、およびフルスクリーンのiOSおよびiPadOSアプリとゲームで、ホーム画面のインジケータのジェスチャを遅らせるためのガイダンスを更新。  
2024年6月10日| フルスクリーンモードでのゲームプレイのガイダンスを改善。
