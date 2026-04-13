# アクションシート

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/action-sheets

# アクションシート

アクションシートは、ユーザが開始したアクションに関連する選択肢を表示するモーダルビューです。

![iPhoneの下部にある図案化されたアクションシートのボタン。画像は全体が、6色のオリジナルAppleロゴを連想させる赤色になっています。](https://docs-assets.developer.apple.com/published/895106967463c0d204bc042eee75ed55/components-action-sheet-intro%402x.png)

デベロッパ向けメモ

SwiftUIで確認ダイアログに[プレゼンテーション修飾子](https://developer.apple.com/documentation/swiftui/view-presentation)を指定すると、すべてのプラットフォームでアクションシート機能を提供できます。UIKitでは[`UIAlertController.Style.actionSheet`](/documentation/UIKit/UIAlertController/Style/actionSheet)を使用すると、iOS、iPadOS、tvOSでアクションシートを表示できます。

## [ベストプラクティス](/jp/design/human-interface-guidelines/action-sheets#Best-practices)

**ユーザが意図したアクションに関連する選択肢を提示する場合は、アラートではなくアクションシートを使用する。** 例えば、iPhoneの「メール」でメッセージの編集をキャンセルする場合は、下書きを削除、または下書きを保存という2つの選択肢がアクションシートで提示されます。アラートは、破壊的な結果につながるアクションの確認やキャンセルを行う場合に役立ちますが、アクションに関連する追加の選択肢を提示することはできません。さらに重要な点として、アラートは通常、ユーザの予期しないタイミングで表示され、ユーザの対応が必要になる可能性がある問題や現在の状況の変化を通知します。ガイダンスは、[アラート](/jp/design/human-interface-guidelines/alerts)を参照してください。

![iPhoneの「メール」で作成中の新規メッセージのスクリーンショットの一部。](https://docs-assets.developer.apple.com/published/97084a38eb0e4f2c70854e4a54ff0739/action-sheet-iphone-mail%402x.png)

![iPhoneの「メール」で作成中の新規メッセージのスクリーンショットの一部。メッセージのキャンセルを選択したあとにアクションシートが開いています。アクションシートで、下書きを削除、または下書きを保存という選択肢が提示されています。](https://docs-assets.developer.apple.com/published/0999d64a6aa1a9ffa4358f3b994219a8/action-sheet-iphone-mail-delete-action%402x.png)

**アクションシートは多用しない。** アクションシートは重要な情報や選択肢を提示しますが、その際に現在のタスクが中断されます。アクションシートに注意が払われるように、必要以上に使用しないようにしてください。

**タイトルは1行で収まる程度に短くする。** 長いタイトルは素早く読み取れず、文字が途中で切れたりスクロールが必要になったりすることもあります。

**メッセージは必要な場合にのみ提示する。** 基本的に現在のアクションが発生した状況が分かっていれば、ユーザはタイトルだけで選択肢を十分に理解できます。

**必要な場合は、データが破壊される可能性があるアクションをキャンセルボタンで取り消せるようにする。** キャンセルボタンはアクションシートの一番下（watchOSの場合はシートの左上隅）に配置します。SwiftUIの確認ダイアログには、デフォルトでキャンセルボタンが含まれています。

**破壊的な選択肢は目立つようにする。** 破壊的なアクションを実行するボタンには、破壊的であることが分かるようなスタイルを適用します。また、こういったボタンは最も目を引くようにアクションシートの一番上に配置します。デベロッパ向けのガイダンスは、[`destructive`](/documentation/SwiftUI/ButtonRole/destructive)（SwiftUI）または[`UIAlertAction.Style.destructive`](/documentation/UIKit/UIAlertAction/Style-swift.enum/destructive)（UIKit）を参照してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/action-sheets#Platform-considerations)

 _macOS、tvOSに追加の考慮事項はありません。visionOSには対応していません。_

### [iOS/iPadOS](/jp/design/human-interface-guidelines/action-sheets#iOS-iPadOS)

**アクションに関連する選択肢を提示する場合は、メニューではなくアクションシートを使用する。** 実行するアクションについてさらに明示的な選択を行う必要がある場合、アクションシートが表示されて、そこから選ぶのがユーザの慣れ親しんだ手順です。一方、ユーザにとって、メニューは自分の意図的な操作で表示させるものです。

**アクションシートはスクロールさせない。** アクションシートにボタンが多いほど、選択に必要な時間と作業が増加します。また、アクションシートをスクロールすると、意図しないボタンをタップしてしまうこともあります。

### [watchOS](/jp/design/human-interface-guidelines/action-sheets#watchOS)

システムで定義されているアクションシートのスタイルには、タイトル、オプションのメッセージ、キャンセルボタン、1つ以上のその他のボタンが含まれています。このインターフェイスの見た目は、デバイスによって異なります。

![Apple Watchのアクションシート。Watchの画面の上半分にテキストがあり、下半分に2つのボタンが縦に並んでいます。](https://docs-assets.developer.apple.com/published/635ef9fbaa57e4f2414277b0ee89f3f8/action-sheet-watch-system-defined%402x.png)

それぞれのボタンには、ボタンがもたらす影響をユーザに伝えるスタイルが適用されます。システムで定義されたボタンには、次の3つのスタイルがあります:

スタイル| 意味  
---|---  
デフォルト| ボタンに特別な意味はありません。  
破壊的| ボタンによってユーザのデータが破壊されるか、アプリで破壊的なアクションが実行されます。  
キャンセル| 何のアクションも実行せず、ビューを閉じます。  
  
**アクションシートに表示するボタンは、キャンセルボタンを含めて4つ以内にする。** 画面に表示するボタンが少ないほど、選択肢を一目で見ることができるようになります。キャンセルボタンは必須なので、追加の選択肢は3つ以下にしてください。

## [リソース](/jp/design/human-interface-guidelines/action-sheets#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/action-sheets#Related)

[モダリティ](/jp/design/human-interface-guidelines/modality)

[シート](/jp/design/human-interface-guidelines/sheets)

[アラート](/jp/design/human-interface-guidelines/alerts)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/action-sheets#Developer-documentation)

[`confirmationDialog(_:isPresented:titleVisibility:actions:)`](/documentation/SwiftUI/View/confirmationDialog\(_:isPresented:titleVisibility:actions:\)-46zbb) — SwiftUI

[`UIAlertController.Style.actionSheet`](/documentation/UIKit/UIAlertController/Style/actionSheet) — UIKit
