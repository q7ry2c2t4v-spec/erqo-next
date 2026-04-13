# ピッカー

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/pickers

# ピッカー

ピッカーは、1つまたは複数のスクロール可能なリストで、ユーザはそこから値を選択できます。

![図案化されたスクロール可能なリスト。項目が選択されています。画像は全体が、6色のオリジナルAppleロゴを連想させる赤色になっています。](https://docs-assets.developer.apple.com/published/cbf555fb6bb88024c36c8f65789f5d9d/components-pickers-intro%402x.png)

ピッカーには複数のスタイルがあり、選択できる値と見た目のタイプがスタイルによって異なっています。ピッカーに表示される値とその順序は、デバイスの言語によって異なります。

ピッカーで、1つまたはマルチパート型の値を選択できるようにすれば、ユーザが情報を入力する助けになります。特に日付ピッカーでは、カレンダービューで日付を選択する、テンキーを使用して日付と時刻を入力するなど、複数の方法で値を選択できるようになっています。

## [ベストプラクティス](/jp/design/human-interface-guidelines/pickers#Best-practices)

**中規模から大規模な項目のリストによる提示にピッカーを使う。** かなり短い選択肢のリストを表示する場合は、ピッカーではなく[プルダウンボタン](/jp/design/human-interface-guidelines/pull-down-buttons)の使用を検討してください。ピッカーの強みは、多くの項目を素早く簡単にスクロールできることです。短い項目リストに使うのは、視覚的な装飾が過剰と考えられます。逆に、超大規模な項目を提示する必要がある場合は、[リストまたはテーブル](/jp/design/human-interface-guidelines/lists-and-tables)の使用を検討してください。リストとテーブルは高さを調整でき、テーブルにはインデックスを設定できます。インデックスによって目的の場所に非常に高速に移動できます。

**値は予測可能で論理的な順番にする。** ユーザがピッカーを操作しようとしても、値の多くが表示されていないという状況があり得ます。目的の項目に素早く移動できるようにするには、国リストをアルファベット順にするなど、表示されていない値をユーザが予測できる順序で並べるのが最善です。

**ピッカーを表示するためにビューを切り替えない。** ピッカーは、ユーザが編集中のフィールドの下や近くなど、操作のコンテキストに合わせて表示するのが効果的です。通常、ピッカーはウインドウの下部またはポップオーバーに表示されます。

**日付ピッカーで分を指定する場合は細かくしすぎないようにする。** デフォルトで、分のリストには60個（0から59）の値が含まれます。オプションで、分と分の間隔を空けることができます（60を均等に分割できる間隔に限ります）。例えば、1時間を4分割した間隔（0、15、30、45）にできます。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/pickers#Platform-considerations)

 _visionOSに追加の考慮事項はありません。_

### [iOS/iPadOS](/jp/design/human-interface-guidelines/pickers#iOS-iPadOS)

日付ピッカーは、タッチ、キーボード、ポインティングデバイスを使用して特定の日付、時刻、またはその両方を選択できる効率的なインターフェイスです。日付ピッカーは、次のいずれかのスタイルで表示できます:

  * コンパクト — 編集可能な日付と時刻のコンテンツがモーダルビューに表示されるボタンです。

  * インライン — 時刻のみの場合は値のホイールを表示するボタン、日付と時刻の場合はインラインカレンダービューです。

  * ホイール — 一連のスクロールするホイールです。内蔵または外部キーボードによるデータ入力にも対応しています。

  * 自動 — 現在のプラットフォームと日付ピッカーモードに応じて、システムがスタイルを決定します。

日付ピッカーには4つのモードがあり、モードによって選択できる値が異なります。

  * 日付 — 月、日、年が表示されます。

  * 時刻 — 時と分が表示され、オプションで午前/午後を指定できます。

  * 日付と時刻 — 日付、時、分が表示され、オプションで午前/午後を指定できます。

  * カウントダウンタイマー — 最大で23時間59分までの時と分が表示されます。このモードは、インラインまたはコンパクトのスタイルでは利用できません。

日付ピッカーに表示される厳密な値とその順序は、デバイスのある場所によって変わります。

スタイルとモードのさまざまな組み合わせを示すいくつかの日付ピッカーの例を以下に示します。

![コンパクト日付ピッカーの図。現在選択されている日付が1行でインライン表示されています。ピッカーは、行の下方向に広がるポップオーバーとして開き、日付を選択するための1か月分のカレンダーが表示されます。](https://docs-assets.developer.apple.com/published/4735b4b3337fc9bfc2405b627bef32d1/pickers-date-picker-compact-expanded%402x.png)コンパクトレイアウトのピッカーは、コンテンツの上にポップオーバーとして開きます。

![「日付」というタイトルが付いたインライン日付ピッカーの図。上部のトグルがオンになっていて、タイトルとトグルの下に日付を選択するための1か月分のカレンダーが表示されています。](https://docs-assets.developer.apple.com/published/2e1c64487940782f05b34a7eef284406/pickers-date-picker-inline-expanded%402x.png)インラインレイアウトのピッカーは、コンテンツ内にインラインで開きます。

![「時刻」というタイトルが付いたインライン時刻ピッカーの図。現在選択されている時刻がタイトル行に表示され、その下に、時間、分、午前/午後の値を選択するための3つの垂直ホイールが表示されています。](https://docs-assets.developer.apple.com/published/5863c89e2cc5ccf221df2433fd82a854/pickers-time-picker-inline-wheel%402x.png)インラインピッカーの別の例。ホイールを使用して日付と時刻の値を選択します。

**スペースが限られている場合はコンパクト日付ピッカーを使う。** コンパクトスタイルでは、アプリのアクセントカラーを使って、ボタンに現在の値が表示されます。ユーザがボタンをタップするとモーダルビューが開き、おなじみのカレンダー形式のエディタと時刻ピッカーを利用できるようになります。モーダルビューの中で日付と時刻を編集し、ビューの外側をタップすると選択が確定します。

### [macOS](/jp/design/human-interface-guidelines/pickers#macOS)

**アプリに適した日付ピッカーのスタイルを選択する。** macOSには、テキストとグラフィカルという2つの日付ピッカースタイルがあります。テキストスタイルは、スペースが限られており、ユーザが特定の日付と時刻を選択すると想定される場合に便利です。グラフィカルスタイルは、ユーザがカレンダーで日付を参照したり日付の範囲を選択したりできるオプションを提供したい場合や、時計の文字盤が似合うアプリの場合に便利です。

デベロッパ向けのガイダンスは、[`NSDatePicker`](/documentation/AppKit/NSDatePicker)を参照してください。

### [tvOS](/jp/design/human-interface-guidelines/pickers#tvOS)

tvOSでは、SwiftUIでピッカーを利用できます。デベロッパ向けのガイダンスは、[`Picker`](/documentation/SwiftUI/Picker)を参照してください。

### [watchOS](/jp/design/human-interface-guidelines/pickers#watchOS)

ピッカーで表示される項目のリスト内を、ユーザがDigital Crownを使用して移動するという、正確かつ洗練された選択操作を提供できます。

ピッカーではホイールスタイルの項目リストを表示できます。watchOSでは、日付や時刻のピッカーをホイールスタイルで表示することも可能です。デベロッパ向けのガイダンスは、[`Picker`](/documentation/SwiftUI/Picker)および[`DatePicker`](/documentation/SwiftUI/DatePicker)を参照してください。

![Apple Watchのピッカービューを含む画面の図。リスト内の3つの項目が表示されています。中央の項目が強調表示されています。](https://docs-assets.developer.apple.com/published/c96f5357ef4e905bf7d543c74710d660/pickers-wheel-watch%402x.png)

![Apple Watchの日付ピッカーを含む画面の図。日が強調表示されています。](https://docs-assets.developer.apple.com/published/c4acbbd16f4d11f874e9ac449693e7b1/pickers-date-watch%402x.png)

![Apple Watchの時刻ビューを含む画面の図。分が強調表示されています。](https://docs-assets.developer.apple.com/published/71374008f488021c4bb37e52e1faabf5/pickers-time-watch%402x.png)

アウトライン、キャプション、スクロールインジケータを表示するようにピッカーを設定できます。

リストが長い場合、ナビゲーションリンクはピッカーをボタンとして表示します。ユーザがそのボタンをタップすると、オプションのリストが表示されます。または、ボタンをタップせずにDigital Crownを使ってオプションをスクラブで移動することもできます。デベロッパ向けのガイダンスは、[`navigationLink`](/documentation/SwiftUI/PickerStyle/navigationLink)を参照してください。

![Apple Watchのピッカーボタンを含む画面の図。ボタンのテキストによって、2番目の項目を選択中であることが示されています。](https://docs-assets.developer.apple.com/published/c8b94eb368c116076da1c5365babf4dd/pickers-navigation-button-watch%402x.png)

![Apple Watchの項目リストが表示されている画面の図。リストの2番目の項目が選択されています。](https://docs-assets.developer.apple.com/published/b0f2b3c226d24d6db3c58582b7cc6f09/pickers-navigation-list-watch%402x.png)

## [リソース](/jp/design/human-interface-guidelines/pickers#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/pickers#Related)

[プルダウンボタン](/jp/design/human-interface-guidelines/pull-down-buttons)

[リストとテーブル](/jp/design/human-interface-guidelines/lists-and-tables)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/pickers#Developer-documentation)

[`Picker`](/documentation/SwiftUI/Picker) — SwiftUI

[`UIDatePicker`](/documentation/UIKit/UIDatePicker) — UIKit

[`UIPickerView`](/documentation/UIKit/UIPickerView) — UIKit

[`NSDatePicker`](/documentation/AppKit/NSDatePicker) — AppKit

## [変更履歴](/jp/design/human-interface-guidelines/pickers#Change-log)

日付| 変更内容  
---|---  
2023年6月05日| watchOSでのピッカーの使い方に関するガイダンスを更新。
