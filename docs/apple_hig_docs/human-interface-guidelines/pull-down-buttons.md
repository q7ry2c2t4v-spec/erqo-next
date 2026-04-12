# プルダウンボタン

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/pull-down-buttons

# プルダウンボタン

プルダウンボタンには、ボタンの目的に直接関連する項目やアクションで構成されるメニューが表示されます。

![項目を表示している図案化されたプルダウンメニュー。画像は6色のオリジナルAppleロゴをイメージさせる赤色になっています。](https://docs-assets.developer.apple.com/published/b40344755e5449a8478bf1d981ae90d9/components-pull-down-button-intro%402x.png)

ユーザがプルダウンボタンのメニューから項目を選択すると、メニューが閉じ、選択したアクションが実行されます。

## [ベストプラクティス](/jp/design/human-interface-guidelines/pull-down-buttons#Best-practices)

**プルダウンボタンはボタンのアクションに直接関連するコマンドや項目を提示するために使う。** プルダウンボタンのメニューから操作を行うことで、インターフェイスに新たなボタンを追加することなく、アクションの対象を明確にしたり、その動作をカスタマイズしたりすることができます。以下はボタンの例です:

  * ユーザが追加したい項目を指定するためのメニューが呼び出される「追加」ボタン。

  * ユーザが並べ替えの基準となる属性を選択するためのメニューが呼び出される「並べ替え」ボタン。

  * 直前の場所を開く代わりにユーザが戻り先を選択できるメニューが呼び出される「戻る」ボタン。

択一的な項目（コマンド以外）をリスト表示する必要がある場合は、代わりに[ポップアップボタン](/jp/design/human-interface-guidelines/pop-up-buttons)を使用してください。

**ビューのすべてのアクションを1つのプルダウンボタンに収容しない。** ビューの主要なアクションはユーザがすぐに見つけられるようにする必要があります。プルダウンボタンの中に収容すると、そのアクションを実行する前にプルダウンボタンを開く操作が必ず発生するので、主要なアクションには不向きです。

**使いやすさを考えてメニューの長さのバランスをとる。** ユーザがメニューを見るには、プルダウンボタンを操作しなければなりません。そのメニューに2つ以下の項目しか表示されなければ、ボタン操作からのメニュー表示は大げさだとユーザが感じる可能性があります。表示するリストに1つか2つの項目しかない場合は、別のコンポーネントの利用を検討してください。アクションを実行するためのボタン、選択を行うためのトグルやスイッチなどです。反対に、プルダウンボタンのメニュー項目が多すぎると、目的の項目を見つける方に時間がとられ、ユーザの操作スピードが落ちるおそれがあります。

**意味がより明確になる場合にのみ簡潔なメニュータイトルを付ける。** 通常、プルダウンボタンの内容と、分かりやすいメニュー項目によって、ユーザが必要とするコンテキストがすべて提供されるため、メニューのタイトルは必要ありません。

**プルダウンボタンのメニュー項目が破壊的なアクションであることを伝え、ユーザの意図を確認する。** 破壊的な結果をもたらす可能性があるアクションは、赤いテキストで強調表示されます。ユーザが破壊的なアクションを選択すると、システムから[アクションシート](/jp/design/human-interface-guidelines/action-sheets)（iOS）または[ポップオーバー](/jp/design/human-interface-guidelines/popovers)（iPadOS）が表示され、ユーザはそのアクションを実行するかキャンセルするかを決定できます。アクションシートはメニューとは異なる位置に表示され、消去するには意図的な操作が必要なので、ユーザが誤ってデータを失う可能性は低くなります。

**必要であればメニュー項目にインターフェイスアイコンを付ける。** 項目の意味を明確化する必要がある場合は、ラベルのあとに[アイコン](/jp/design/human-interface-guidelines/icons)や画像を表示できます。この目的で[SF Symbols](/jp/design/human-interface-guidelines/sf-symbols)を使用すると、常にテキストのサイズに合ったシンボルを表示でき、慣れ親しんだ操作性をユーザに提供する助けになります。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/pull-down-buttons#Platform-considerations)

 _macOS、visionOSに追加の考慮事項はありません。tvOSとwatchOSには対応していません。_

### [iOS/iPadOS](/jp/design/human-interface-guidelines/pull-down-buttons#iOS-iPadOS)

注意

ユーザがボタンの上で特定のジェスチャをするとプルダウンメニューが開くようにすることもできます。例えばiOS 14以降のSafariでは、タブボタンをタッチして押さえたままにするジェスチャで、「新規タブ」や「タブをすべて閉じる」などのタブ関連のアクションのメニューが表示されます。

**メインインターフェイスの目立つ位置に表示する必要のない項目を「さらに表示」プルダウンボタンを使って提示する。** スペースに制約がある場合、一部の項目を「さらに表示」ボタンで表示するようにするとスペースの節約になりますが、それらの項目が見つけにくくなるという副作用があります。一般にユーザは、現在の状況に関連する付加的な機能が「さらに表示」ボタンから提供されることを知っていますが、ユーザが省略記号アイコンから中身を正しく推測できるとは限りません。効果的な「さらに表示」ボタンを設計するには、スペース節約の効用と項目を見つけにくくなるという副作用を比較検討し、アプリに最適なバランスを判断する必要があります。

![iPhoneのメモアプリのスクリーンショット。「Nature Walks」というタイトルの「メモ」の書類が開いています。上部のツールバーの末尾側にその他ボタンが含まれています。](https://docs-assets.developer.apple.com/published/1ad6dfa5e504822ececb37f22bf73335/menu-secondary-actions-collapsed%402x.png)

![iPhoneのメモアプリのスクリーンショット。「Nature Walks」というタイトルの「メモ」の書類が開いています。上部のツールバーのその他ボタンが展開されて、追加の機能を含む「その他」メニューが表示されています。](https://docs-assets.developer.apple.com/published/abaf48ff068bfeb4b0aedaf197c13b71/menu-secondary-actions-expanded%402x.png)

## [リソース](/jp/design/human-interface-guidelines/pull-down-buttons#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/pull-down-buttons#Related)

[ポップアップボタン](/jp/design/human-interface-guidelines/pop-up-buttons)

[ボタン](/jp/design/human-interface-guidelines/buttons)

[メニュー](/jp/design/human-interface-guidelines/menus)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/pull-down-buttons#Developer-documentation)

[`MenuPickerStyle`](/documentation/SwiftUI/MenuPickerStyle) — SwiftUI

[`showsMenuAsPrimaryAction`](/documentation/UIKit/UIControl/showsMenuAsPrimaryAction) — UIKit

[`pullsDown`](/documentation/AppKit/NSPopUpButton/pullsDown) — AppKit

## [変更履歴](/jp/design/human-interface-guidelines/pull-down-buttons#Change-log)

日付| 変更内容  
---|---  
2022年9月14日| 使いやすいメニューの長さの設計に関するガイドを改訂。
