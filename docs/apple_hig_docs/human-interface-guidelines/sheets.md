# シート

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/sheets

# シート

シートは、現在のコンテキストと密接に関連する、範囲の限定されたタスクの実行に役立ちます。

![図案化されたシート。ウインドウの上から下に延びています。画像は全体が、6色のオリジナルAppleロゴを連想させる赤色になっています。](https://docs-assets.developer.apple.com/published/a8b4a36007724701985fbacd8152218c/components-sheet-intro%402x.png)

シートはデフォルトで _モーダル_ です。つまり、表示されたシートでの操作を完了してシートを閉じるまで、親ビューを操作することはできません（モーダル表示について詳しくは、[モダリティ](/jp/design/human-interface-guidelines/modality)を参照してください）。モーダルシートは、特定の情報をユーザにリクエストする場合や、簡単なタスクを提示してユーザがそれを完了するまでは親ビューに戻れないようにしたい場合に便利です。例えば、ファイルを添付する、移動先または保存先の場所を選択する、選択項目のフォーマットを指定する、などのアクションの完了に必要な情報の入力をユーザに求める状況では、シートの使用をおすすめします。

macOS、visionOS、watchOSではシートは常にモーダルですが、iOSとiPadOSではシートがモーダルでないこともあります。モーダルでないシートが表示されている場合、ユーザはそのシートを開いたまま、親ビューの現在のタスクを直接続行できます。例えば、iPhoneとiPadの「メモ」では、選択したさまざまなテキストに異なる書式を簡単に適用できる、モーダルでないシートを使用しながら、親ビューでメモの編集作業を続行できます。

![iPhoneで編集中のメモ。複数の単語が選択され、強調表示されています。画面下半分のフォーマットシートで、選択した単語をレギュラーの本文フォントで表示するように指定しています。](https://docs-assets.developer.apple.com/published/33d32924d110c7105e051b281c7d98ed/sheets-nonmodal-notes-text-regular%402x.png)

「メモ」のフォーマットシートを使用すると、編集ビューで選択されているテキストに書式を適用できます。

![iPhoneで編集中の同じメモ。別の単語が選択され、強調表示されています。フォーマットシートで、選択した単語をイタリックの本文フォントで表示するように指定しています。](https://docs-assets.developer.apple.com/published/a32faae381817efc311f69c4dd7900b4/sheets-nonmodal-notes-text-italic%402x.png)

このシートはモーダルでないため、シートを開いたまま次のテキストを選択できます。

## [ベストプラクティス](/jp/design/human-interface-guidelines/sheets#Best-practices)

**シートは、シンプルなコンテンツまたはタスクを表示するときに使う。** シートを開いても親ビューの一部は見えたままなので、シートには、ユーザが親ビューのコンテキストを念頭に置きながら操作できるという特長があります。

**ユーザフローが複雑な場合や長い場合はシートの代わりになるものを検討する。** 例えば、iOSとiPadOSのモーダルビューはフルスクリーンスタイルで、ビデオ、写真、カメラビューなどのコンテンツを表示したり、書類または写真編集などのマルチステップタスクを実行したりするのに適しています。（デベロッパ向けのガイダンスは、[`UIModalPresentationStyle.fullScreen`](/documentation/UIKit/UIModalPresentationStyle/fullScreen)を参照してください。）macOSでは、シートを使用する代わりに、新しいウインドウを開くかフルスクリーンモードに移行できるようにするとよいでしょう。例えば、書類を編集するような自己完結型のタスクは別個のウインドウを開いた方がやりやすいことが多く、メディアの閲覧には[フルスクリーンモード](/jp/design/human-interface-guidelines/going-full-screen)が適しています。visionOSでは、コンテンツやタスクにイマーシブな空間に入ることができるフルスペースに移行する方法をアプリで提供できます。ガイダンスは、[イマーシブ体験](/jp/design/human-interface-guidelines/immersive-experiences)を参照してください。

**メインインターフェイスからは一度に1つだけシートを表示する。** ほとんどのユーザは、シートを閉じると、親ビューまたは親ウインドウに戻ると考えます。シートを閉じたときの戻り先が別のシートになると、ユーザがアプリの操作の流れを見失ってしまうおそれがあります。シートの中で操作を行った結果、別のシートが表示される場合は、最初のシートを閉じてから新しいシートを開いてください。必要な場合は、2つ目のシートが閉じられたときに最初のシートを開き直します。

**モーダルでないビューは、親ビューのメインタスクに影響する補足的な項目を表示したい場合に使用する。** メインウインドウを操作しているときに、必要とする情報やアクションにユーザがアクセスできるようにするには、visionOSでは[分割ビュー](/jp/design/human-interface-guidelines/split-views)、macOSでは[パネル](/jp/design/human-interface-guidelines/panels)を使用することを検討しましょう。iOSとiPadOSでは、モーダルでないシートをこのワークフローで使用できます。ガイダンスは、[iOS、iPadOS](/jp/design/human-interface-guidelines/sheets#iOS-iPadOS)を参照してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/sheets#Platform-considerations)

 _tvOSに追加の考慮事項はありません。_

### [iOS/iPadOS](/jp/design/human-interface-guidelines/sheets#iOS-iPadOS)

サイズ変更可能なシートは、ユーザがコンテンツをスクロールしたり、 _グラバー_ をドラッグしたりしたときにサイズが変わります。グラバーは小さな水平インジケータで、シートの上端に表示されます。シートのサイズは、 _ディテント_ に従って変更されます。ディテントとは、シートが自然に収まる特定の高さのことです。ディテントはiPhone向けにデザインされており、シートが自然に収まる特定の高さがあらかじめ設定されています。システムでは、2つのディテントが定義されています: _ラージ_ はシートが完全に展開された高さで、 _ミディアム_ はその約半分です。

![縦向きのiPhoneイラスト。画面のほぼ全体を覆っている角丸四角形（フルスクリーンシート）が表示されています。シートの左上隅に、丸い「閉じる」ボタンが表示されます。](https://docs-assets.developer.apple.com/published/c2a600adb5237892585d71d2ae61c9a6/sheets-large-detent%402x.png)

ラージのディテント

![縦向きのiPhoneイラスト。画面の半分を覆っている角丸四角形（ハーフスクリーンシート）が表示されています。シートの左上隅に、丸い「閉じる」ボタンが表示されます。](https://docs-assets.developer.apple.com/published/413ac0d4cf462891f2ba9d0cd4bb01f1/sheets-medium-detent%402x.png)

ミディアムのディテント

シートは自動的にラージのディテントに対応します。これにミディアムのディテントを追加すると、シートがいずれかの高さに収まるようになります。ミディアムだけを指定すると、シートを画面全体に拡大できなくなります。デベロッパ向けのガイダンスは、[`detents`](/documentation/UIKit/UISheetPresentationController/detents)を参照してください。

**iPhoneアプリでは、ミディアムのディテントに対応してシートのコンテンツの段階的な表示を検討する。** 例えば共有シートでは、ミディアムのディテントのままサイズを変更しなくても、関連するほとんどの項目を表示できます。ほかの項目を表示したいユーザは、シートをスクロールするか拡大できます。画面全体にシートのコンテンツを表示する方が便利な場合は、ミディアムのディテントに対応しないという設計も考えられます。例えば、「メッセージ」や「メール」の新規作成シートは、十分なスペースを使ってコンテンツを作成できるように、ラージのディテントでのみ表示されます。

**サイズ変更可能なシートにはグラバーを含める。** グラバーは、シートをドラッグしてサイズ変更できることを示します。また、グラバーをタップすると、ディテントを順番に選択できます。シートがサイズ変更可能かどうかが、グラバーの有無で分かるようにします。グラバーはVoiceOverにも対応しており、ユーザは画面を見ずにシートのサイズを変更できます。デベロッパ向けのガイダンスは、[`prefersGrabberVisible`](/documentation/UIKit/UISheetPresentationController/prefersGrabberVisible)を参照してください。

**スワイプでシートを閉じられるようにする。** ほとんどのユーザは、閉じるボタンをタップしても、そうしないで縦にスワイプしてもシートを閉じられると考えます。シートに保存していない変更がある状態で、ユーザがスワイプで閉じる操作を行った場合は、閉じるアクションを続行するかどうかアクションシートを使用して確認してください。

**ユーザの期待に沿って、「完了」ボタンと「キャンセル」ボタンを配置する。** 通常、「完了」または「閉じる」ボタンはシートの右上隅（左から右へのレイアウト）に配置します。「キャンセル」ボタンは、シートの左上隅に配置します。

追加のサブビューがあるシートは例外で、「キャンセル」ボタンは右上に配置します。これにより、2ページ目以降のページの左上に「戻る」ボタンを配置する場所ができます。ナビゲーションフローの最後では、「キャンセル」ボタンを「完了」ボタンで置き換えます。

![iPhoneのシートの上半分の図。ビューの左上隅に「キャンセル」ボタンがあります。](https://docs-assets.developer.apple.com/published/4c0ea03add08b05592c51ed58ebb79f1/sheets-close-button-placement-no-back%402x.png)

「キャンセル」ボタンを単独で表示する場合の配置

![iPhoneのシートの上半分の図。ビューの左上隅に「戻る」ボタンが表示され、右上隅に「キャンセル」ボタンが表示されています。](https://docs-assets.developer.apple.com/published/4325d8e5db78c585b01a7137e34189c7/sheets-close-button-placement-with-back%402x.png)

複数ステップからなるフローの一部として表示する場合の「キャンセル」ボタンの配置

**iPadOSアプリでは、ページまたはフォームのシート表示スタイルを優先的に使用する。** 各スタイルでは、暗めのバックグラウンドビューの上に中央揃えでコンテンツが配置され、シートにデフォルトのサイズが使用されるので、一貫性のある体験が提供されます。デベロッパ向けのガイダンスは、[`UIModalPresentationStyle`](/documentation/UIKit/UIModalPresentationStyle)を参照してください。

### [macOS](/jp/design/human-interface-guidelines/sheets#macOS)

macOSのシートは、親ウインドウの上にフロート表示される角の丸いカードのようなビューになります。シートが画面に表示されている間、親ウインドウは暗くなります。これは、シートを閉じるまで親ウインドウを操作できないという意味です。ただし一般には、シートを開いたままでも、ほかのアプリのウインドウは操作できます。

![メモアプリのスクリーンショット。背景にある暗くなった「メモ」の書類の上部中央に「メモの新機能」というシートがあります。](https://docs-assets.developer.apple.com/published/2e4aef35250535ffce6aaf467275386d/sheets-macos-notes%402x.png)

**妥当なデフォルトサイズでシートを表示する。** 通常、ユーザはシートのサイズを変更できるとは考えません。そのため、表示するコンテンツに適したサイズを使用することは重要です。ただし、コンテンツを拡大してはっきり見えるようにする必要があるなど、シートのサイズを変更できるようにする方が適切と考えられる場合には、サイズ変更に対応することをおすすめします。

**シートを閉じなくてもアプリのほかのウインドウを操作できるようにする。** シートが開くときは、その親ウインドウが前面に移動しています。親ウインドウが書類ウインドウの場合は、書類に関連するモードレスなパネルも前面に移動します。ユーザがアプリのほかのウインドウを操作できるようにしたい場合は、シートを閉じなくてもそれらのウインドウを前面に移動できるようにしてください。

**シートを閉じるボタンをユーザが想定する位置に表示する。** ほとんどのユーザは、「完了」、「OK」、「キャンセル」などのシートを閉じるボタンが、すべてビューの下の末尾側に表示されていると考えます。

**ユーザが入力して結果を確認する操作を繰り返す場合は、シートではなくパネルを使う。** 例えば、検索と置換パネルで、ユーザが置換を実行するたびに結果を確認できるようにするとよいでしょう。ガイダンスは、[パネル](/jp/design/human-interface-guidelines/panels)を参照してください。

### [visionOS](/jp/design/human-interface-guidelines/sheets#visionOS)

シートは、visionOSアプリ内で表示されている間は親ウインドウの前に浮かびます。このとき、親ウインドウは暗くなり、シートがユーザの操作対象になります。

以下のカスタムコントロールを使用できます 

このビデオコンテンツの説明: visionOSの空のウインドウの上で開いているシートを示している録画。 

再生 

**シートをウインドウの下端から表示することは避ける。** ユーザにとってシートが見やすくなるように、ユーザの[視野](/jp/design/human-interface-guidelines/spatial-layout#Field-of-view)の中央に配置することをおすすめします。

**ユーザがコンテキストに留まれるようにシートはデフォルトサイズで提示する。** シートでウインドウの大部分や全体を覆うことは避け、シートのサイズ変更はユーザの判断に任せることを検討してください。

### [watchOS](/jp/design/human-interface-guidelines/sheets#watchOS)

watchOSのシートは、アプリの現在のコンテンツにスライドして重なるフルスクリーンビューです。現在のコンテキストを維持できるように、シートは半透明になっていますが、シートの背景には下にあるコンテンツがぼやけて暗めになるマテリアルが適用されます。

![Apple Watchのシートのスクリーンショット。プライマリアクションボタンとデフォルトのキャンセルボタンがあります。](https://docs-assets.developer.apple.com/published/fa2be238df5f87148ef57bbde2378ac9/sheets-watch-overlay%402x.png)

**モーダルタスクでカスタムのタイトルやコンテンツを提示する必要がある場合にのみ、シートを使う。** ユーザに重要な情報を提供したり、一連の選択肢を提示したりする必要がある場合は、[アラート](/jp/design/human-interface-guidelines/alerts)や[アクションシート](/jp/design/human-interface-guidelines/action-sheets)の使用を検討してください。

**シートの操作は簡潔にし多用しない。** シートは、現在のワークフローを一時的に中断し、重要なタスクを実行しやすくする目的でのみ使用します。アプリのコンテンツ内を移動しやすくする目的でシートを使用しないでください。

**閉じるコントロールのデフォルトのラベルの変更は、アプリに適切と考えられる場合に限る。** デフォルトで、シートの左上隅には丸い「キャンセル」ボタンが表示されます。アプリの動作やデータを変更するシートには、このボタンを使用します。タスクを実行するのではなく情報を表示するだけのシートでは、代わりに標準の「完了」ボタンを使用します。複数のボタンを表示する場合は、[ツールバー](/jp/design/human-interface-guidelines/toolbars)を使用できます。

![Apple Watchのスクリーンショット。標準のチェックマークの「完了」ボタンがあるシートが表示されています。](https://docs-assets.developer.apple.com/published/bc70ac8a01bd110befa02132e9f53672/sheets-watch-custom%402x.png)

標準の「完了」ボタン

**デフォルトのラベルを変更する場合は、アクションを表すSF Symbolsの使用を優先する。** シートが階層型ナビゲーションインターフェイスの一部であるとユーザが誤解する可能性のあるラベルは使用しないでください。また、上端の先頭にあるテキストをページやアプリのタイトルのようにすると、ユーザはシートの閉じ方が分からなくなります。ガイダンスは、[標準のアイコン](/jp/design/human-interface-guidelines/icons#Standard-icons)を参照してください。

![Apple Watchの画面。上部のツールバーに、デフォルトの「キャンセル」ボタンが表示されています。](https://docs-assets.developer.apple.com/published/4b2b3901392b3a2101bf98fbee0b7809/modal-sheet-watchos-do%402x.png)

![丸に囲まれたチェックマークは正しい使い方を示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

![Apple Watchの画面。上部のツールバーに、カスタムの「戻る」ボタンが表示されています。](https://docs-assets.developer.apple.com/published/3342cdf046b51d5b7e22008f4fa36cf8/modal-sheet-watchos-do-not-1%402x.png)

![丸に囲まれた×印は不適切な使い方を示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![Apple Watchの画面。上部のツールバーに、ページのタイトルを示すボタンが表示されています。](https://docs-assets.developer.apple.com/published/ff5ff3fa9c5591ef7980e7aacb51212a/modal-sheet-watchos-do-not-2%402x.png)

![丸に囲まれた×印は不適切な使い方を示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

## [リソース](/jp/design/human-interface-guidelines/sheets#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/sheets#Related)

[モダリティ](/jp/design/human-interface-guidelines/modality)

[アクションシート](/jp/design/human-interface-guidelines/action-sheets)

[ポップオーバー](/jp/design/human-interface-guidelines/popovers)

[パネル](/jp/design/human-interface-guidelines/panels)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/sheets#Developer-documentation)

[`sheet(item:onDismiss:content:)`](/documentation/SwiftUI/View/sheet\(item:onDismiss:content:\)) — SwiftUI

[`UISheetPresentationController`](/documentation/UIKit/UISheetPresentationController) — UIKit

[`presentAsSheet(_:)`](/documentation/AppKit/NSViewController/presentAsSheet\(_:\)) — AppKit

## [変更履歴](/jp/design/human-interface-guidelines/sheets#Change-log)

日付| 変更内容  
---|---  
2024年3月29日| iPadOSアプリでフォームまたはページのシートスタイルを使用することに関するガイドを追加。  
2023年12月05日| visionOSアプリで補助項目の表示に分割ビューを使用することを推奨。  
2023年6月21日| visionOSのガイダンスを追加するために更新。  
2023年6月05日| watchOSでのシートの使い方に関するガイダンスを更新。
