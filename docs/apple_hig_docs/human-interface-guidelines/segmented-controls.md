# セグメントコントロール

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/segmented-controls

# セグメントコントロール

セグメントコントロールは、2つ以上のセグメントが直線状に並んだもので、それぞれがボタンとして機能します。

![図案化されたセグメントコントロールの選択されたセグメント。画像は全体が、6色のオリジナルAppleロゴを連想させる赤色になっています。](https://docs-assets.developer.apple.com/published/20a5b6bbb2bf19239b94392e611eebab/components-segmented-control-intro%402x.png)

通常、セグメントコントロール内のすべてのセグメントの幅は同じです。[ボタン](/jp/design/human-interface-guidelines/buttons)と同じように、セグメントにはテキストや画像を割り当てられます。セグメントの下（またはコントロール全体の下）にテキストラベルを付けることもできます。

セグメントコントロールでは一連の選択肢から1つの選択肢を選ぶことができ、macOSにはセグメントを1つ選択するタイプと複数選択できるタイプがあります。例えばmacOSのKeynoteでは、選択したテキストを揃えるための配置オプションコントロールで、セグメントを1つだけ選択できます。一方、フォント属性コントロールでは、複数のセグメントを選択してボールド、イタリック、アンダーラインなどのスタイルを組み合わせることができます。Keynoteウインドウのツールバーでも、メインウインドウ領域にさまざまな編集パネルを表示したり非表示にしたりするために、セグメントコントロールを使用しています。

![セグメントコントロールの一部。4つのテキスト配置オプションで構成されています。中央揃えオプションが選択されています。](https://docs-assets.developer.apple.com/published/8c06202270aa61dbeb3f3f76525c2cf2/segmented-control-one-choice%402x.png)単一選択

![セグメントコントロールの一部。4つのフォントの種類で構成されています。4つのオプションのうち3つが選択されています。](https://docs-assets.developer.apple.com/published/2bf53dbb73a0ff0fddca2a07a6e72923/segmented-control-multiple-choices%402x.png)複数選択

セグメントコントロールは、1つまたは複数のセグメントの選択状態を表すことに加え、選択状態を示さずにアクションを実行する一連のボタンとして機能することもできます。例えば、macOSの「メール」の「返信」、「全員に返信」、「転送」ボタンがこれに当たります。デベロッパ向けのガイダンスは、[`isMomentary`](/documentation/UIKit/UISegmentedControl/isMomentary)および[`NSSegmentedControl.SwitchTracking.momentary`](/documentation/AppKit/NSSegmentedControl/SwitchTracking/momentary)を参照してください。

## [ベストプラクティス](/jp/design/human-interface-guidelines/segmented-controls#Best-practices)

**密接な関係にあってオブジェクト、状態、表示に影響を与える選択肢でセグメントコントロールを構成する。** 例えば、インスペクタ内のセグメントコントロールでは、ユーザが1つまたは複数の属性を選択して選択範囲に適用でき、ツールバー内のセグメントコントロールでは、現在のビューで実行する一連のアクションを提示できます。

![iOSのヘルスケアアプリの「アクティビティ」画面の上半分のスクリーンショット。ムーブとエクササイズのアクティビティのグラフが表示されています。グラフの上にあるセグメントコントロールで「日」が選択され、グラフに1日のアクティビティが表示されていることを示しています。](https://docs-assets.developer.apple.com/published/88b0f3f314c66c53072bb5f45a157b18/segmented-controls-activity-charts%402x.png)

iOSのヘルスケアアプリでは、セグメントコントロールで表示するアクティビティのグラフの時間範囲を選択できます。

**機能を1つにまとめることや選択状態を明確に示すことが重要な場合は、セグメントコントロールを検討する。** セグメントコントロールでは、ほかのボタンスタイルとは異なり、ビューのサイズや表示場所に関係なくグループ構造が保持されます。このグループ構造により、どのコントロールが選択されているかをユーザが一目で理解することもできます。

**1つのセグメントコントロール内でコントロールの種類の一貫性を保つ。** コントロールの選択状態を表現するセグメントには、アクションを割り当てないでください。また、アクションを実行するコントロールには、セグメントの選択状態を表示しないようにしてください。

**コントロールのセグメントの数を制限する。** セグメントの数が多すぎると、全体の関係を把握しにくくなり、操作に手間取ります。セグメントの数は、幅広のインターフェイスで5～7個以内、iPhoneで約5個以内に抑えてください。

**セグメントのサイズは基本的に同じにする。** すべてのセグメントを同じ幅にすると、セグメントコントロールのバランスがよくなります。アイコンやタイトルの幅も、可能な範囲で一定にすることをおすすめします。

## [コンテンツ](/jp/design/human-interface-guidelines/segmented-controls#Content)

**1つのセグメントコントロールにテキストと画像を混在させず、なるべくどちらか一方だけを使用する。** 個々のセグメントにはテキストラベルまたは画像を含めることができますが、1つのコントロールに両方のパターンを混在させると、まとまりのない分かりにくいインターフェイスになるおそれがあります。

**各セグメントのコンテンツをできる限り同じようなサイズにする。** 通常はすべてのセグメントの幅が同じになるため、コンテンツが幅いっぱいのセグメントとそうでないセグメントが混在すると、見栄えが悪くなります。

**セグメントのラベルには名詞または名詞句を使用する。** 各セグメントを説明し、[タイトルとしてふさわしいスタイル](https://support.apple.com/guide/applestyleguide/c-apsgb744e4a3/web#apdca93e113f1d64)を使用するテキストを書きましょう。テキストラベルのあるセグメントコントロールに紹介テキストは必要ありません。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/segmented-controls#Platform-considerations)

 _watchOSには対応していません。_

### [iOS/iPadOS](/jp/design/human-interface-guidelines/segmented-controls#iOS-iPadOS)

**密接に関連するサブビューをセグメントコントロールで切り替えることを検討する。** セグメントコントロールは、関連するサブビューを素早く切り替える方法として便利です。例えば、「カレンダー」の「新規予定」シートのセグメントコントロールで、新規予定と新規リマインダーを作成するサブビューを切り替えます。アプリで完全に分離されたセクションを切り替える場合は、代わりに[タブバー](/jp/design/human-interface-guidelines/tab-bars)を使用してください。

![iOSのカレンダーアプリの上半分のスクリーンショット。「新規予定」シートが表示されています。セグメントコントロールで、新規予定と新規リマインダーのどちらを追加するかを切り替えることができます。](https://docs-assets.developer.apple.com/published/05df5d8d9b46440b066c2a7a4f56c0f9/segmented-controls-calendar-new-event%402x.png)

### [macOS](/jp/design/human-interface-guidelines/segmented-controls#macOS)

**紹介テキストを使ってセグメントコントロールの目的を明確にすることを検討する。** セグメントコントロールでシンボルやインターフェイスアイコンを使用する場合は、各セグメントの下にその意味を明確にするラベルを追加できます。アプリにツールチップを含める場合は、セグメントコントロールの各セグメントにツールチップを付けてください。

**メインウインドウ領域では、表示の切り替えにセグメントコントロールではなくタブビューを使用する。**[タブビュー](/jp/design/human-interface-guidelines/tab-views)を使うと、ビューを効率的に切り替えられるようになります。タブビューの見た目は[ボックス](/jp/design/human-interface-guidelines/boxes)とセグメントコントロールを組み合わせたものに似ています。セグメントコントロールは、ツールバーやインスペクタパネルの表示内容の切り替えに適しています。

![macOSのカレンダーアプリのスクリーンショット。メインウインドウ領域に、「日」、「週」、「月」、「年」の4つのタブを含むタブビューが表示されています。サイドバーには、「新規」と「返信済み」の2つのセグメントを含むセグメントコントロールが表示されています。](https://docs-assets.developer.apple.com/published/73d2d9ed60b97456da0a97664ede7dd9/macos-calendar-tab-view-segmented-control-comparison%402x.png)

**スプリングローディングに対応する。** Magic Trackpadを装備したMacでは、選択した項目をドラッグしてドロップせずに強めのクリックをすると、スプリングローディングでセグメントをアクティベートできます。セグメントがアクティベートされたあとも項目をドラッグし続けることができます。

### [tvOS](/jp/design/human-interface-guidelines/segmented-controls#tvOS)

**コンテンツフィルタを実行する画面では、セグメントコントロールではなく分割ビューを使用する。** 多くの場合、分割ビューを使用すると、コンテンツとフィルタオプションの間を簡単に移動できます。セグメントコントロールは、それほど簡単に操作できない場所に表示される可能性があります。

**フォーカスを設定できる要素をセグメントコントロールの近くに配置しない。** セグメントの選択は、ユーザがクリックしたときではなく、セグメントにフォーカスが移動したときに行われます。セグメントコントロールとほかのインターフェイス要素をまとめて配置するときは、両者の位置関係を慎重に検討してください。ほかのフォーカス可能な要素の場所が近すぎると、ユーザがセグメントを切り替えようとしたときに、誤ってその要素にフォーカスが移動するおそれがあります。

### [visionOS](/jp/design/human-interface-guidelines/segmented-controls#visionOS)

ユーザがアイコンを使用するセグメントコントロールを見つめると、割り当て済みの説明テキストが含まれるツールチップが表示されます。

## [リソース](/jp/design/human-interface-guidelines/segmented-controls#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/segmented-controls#Related)

[分割ビュー](/jp/design/human-interface-guidelines/split-views)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/segmented-controls#Developer-documentation)

[`segmented`](/documentation/SwiftUI/PickerStyle/segmented) — SwiftUI

[`UISegmentedControl`](/documentation/UIKit/UISegmentedControl) — UIKit

[`NSSegmentedControl`](/documentation/AppKit/NSSegmentedControl) — AppKit

## [変更履歴](/jp/design/human-interface-guidelines/segmented-controls#Change-log)

日付| 変更内容  
---|---  
2023年6月21日| visionOSのガイダンスを追加するために更新。
