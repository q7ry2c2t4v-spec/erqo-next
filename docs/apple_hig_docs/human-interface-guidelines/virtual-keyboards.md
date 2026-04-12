# 仮想キーボード

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/virtual-keyboards

# 仮想キーボード

物理キーボードを搭載しないデバイスには、ユーザがデータを入力するために使用できる、さまざまなタイプの仮想キーボードが用意されています。

![図案化されたテンキー。デザインツールのキャンバスを思わせるグリッドの上に重ねて表示されてます。画像全体が、6色の初代Appleロゴの赤色を連想させる赤みを帯びています。](https://docs-assets.developer.apple.com/published/d5cea0a3ccb2af2881ade732675a1064/components-virtual-keyboard-intro%402x.png)

仮想キーボードでは、現在のタスクに最適なキーセットを提供できます。例えば、メールアドレスの入力に対応するキーボードには、「@」文字とピリオドを含めることができます。「.com」を含めることもできます。 仮想キーボードはキーボードショートカットに対応していません。

必要に応じて、システムが提供するキーボードの代わりに、アプリ固有のデータ入力に対応するカスタムビューを表示できます。 iOS、iPadOS、tvOSでは、ユーザがインストールして標準キーボードの代わりに使うことができるカスタムキーボードを提供する、アプリ機能拡張を作成することもできます。

## [ベストプラクティス](/jp/design/human-interface-guidelines/virtual-keyboards#Best-practices)

**ユーザが編集しているコンテンツタイプに一致するキーボードを選択する。** 例えば、数字と句読点だけのキーボードの方が、数値データを入力しやすくなります。テキスト入力領域の使用目的を指定すると、想定される入力タイプに適したキーボードがシステムから自動的に表示されます。この情報がキーボードの補正機能の改良に利用される場合もあります。デベロッパ向けのガイダンスは、[`keyboardType(_:)`](/documentation/SwiftUI/View/keyboardType\(_:\))（SwiftUI）、[`textContentType(_:)`](/documentation/SwiftUI/View/textContentType\(_:\))（SwiftUI）、[`UIKeyboardType`](/documentation/UIKit/UIKeyboardType)（UIKit）、および[`UITextContentType`](/documentation/UIKit/UITextContentType)（UIKit）を参照してください。

![iPhoneのキーボードの一部。26文字すべてのキーと、Shift、削除、数字、スペース、Returnキーが表示されます。キーボードの上に入力候補が、下に音声入力ボタンが表示されています。](https://docs-assets.developer.apple.com/published/354d7e53ba3a3d34dff6ab8ae6344410/virtual-keyboard-ascii-capable%402x.png)

![iPhoneのキーボードの一部。10個の数字すべてと削除キーが表示されています。2から9の数字キーには、3文字または4文字のアルファベットが関連付けられています。](https://docs-assets.developer.apple.com/published/0306dc90faeafd6011c9104715fb9678/virtual-keyboard-ascii-capable-number-pad%402x.png)

![iPhoneのキーボードの一部。10個の数字すべてと、削除とピリオドのキーが表示されています。2から9の数字キーには、3文字または4文字のアルファベットが関連付けられています。](https://docs-assets.developer.apple.com/published/4654cbd23d4001644a12b8ae5a5c379a/virtual-keyboard-decimal-pad%402x.png)

![iPhoneのキーボードの一部。26文字すべてのキーと、Shift、削除、数字、スペース、Returnキーが表示されます。キーボードの上に入力候補が、下に絵文字ボタンと音声入力ボタンが表示されています。](https://docs-assets.developer.apple.com/published/7ed801f2abf8863a04540b1c51dc2819/virtual-keyboard-default%402x.png)

![iPhoneのキーボードの一部。26文字すべてのキーと、Shift、削除、数字、スペース、ピリオド、アットマーク記号、Returnキーが表示されます。キーボードの上に入力候補が、下に絵文字ボタンが表示されています。](https://docs-assets.developer.apple.com/published/752bd9d5f3f80fdbb2bda56db1338d73/virtual-keyboard-email-address%402x.png)

![iPhoneのキーボードの一部。26文字すべてのキーと、Shift、削除、数字、スペース、Returnキーが表示されます。キーボードの上に入力候補が、下に絵文字ボタンと音声入力ボタンが表示されています。](https://docs-assets.developer.apple.com/published/be539024350aceb20737393de3442c3a/virtual-keyboard-name-phone-pad%402x.png)

![iPhoneのキーボードの一部。10個の数字すべてと削除キーが表示されています。2から9の数字キーには、3文字または4文字のアルファベットが関連付けられています。](https://docs-assets.developer.apple.com/published/657ae326ff430786dcbef93e2b1decef/virtual-keyboard-number-pad%402x.png)

![iPhoneのキーボードの一部。10個の数字と15個の句読点のキー、副次的な句読点キー、削除、文字、スペース、Returnキーが表示されます。キーボードの上に入力候補が、下に音声入力ボタンが表示されています。](https://docs-assets.developer.apple.com/published/3b741002b38a78ef959a1b45cc618f59/virtual-keyboard-numbers-and-punctuation%402x.png)

![iPhoneのキーボードの一部。10個の数字すべてに加え、削除キーとプラス、スター、ハッシュキーが表示されています。2から9の数字キーには、3文字または4文字のアルファベットが関連付けられています。](https://docs-assets.developer.apple.com/published/a32da49ec2c46031ba620b265bdb5b70/virtual-keyboard-phone-pad%402x.png)

![iPhoneのキーボードの一部。26文字すべてのキーと、Shift、削除、数字、スペース、アットマーク記号、ハッシュキーが表示されます。キーボードの上に入力候補が、下に絵文字ボタンと音声入力ボタンが表示されています。](https://docs-assets.developer.apple.com/published/21a041d7cddd55006393e5f76fb0e6f4/virtual-keyboard-twitter%402x.png)

![iPhoneのキーボードの一部。26文字すべてのキーと、Shift、削除、数字、ピリオド、スラッシュ、.com、Returnキーが表示されます。キーボードの上に入力候補が、下に絵文字ボタンが表示されています。](https://docs-assets.developer.apple.com/published/5392708380ddcbec254ffa07e1717d80/virtual-keyboard-url%402x.png)

![iPhoneのキーボードの一部。26文字すべてのキーと、Shift、削除、数字、スペース、ピリオド、Goキーが表示されます。キーボードの上に入力候補が、下に絵文字ボタンと音声入力ボタンが表示されています。](https://docs-assets.developer.apple.com/published/901970f9f2929b4d461e273ce5987403/virtual-keyboard-web-search%402x.png)

**テキスト入力操作が明確になる場合は、Returnキータイプをカスタマイズする。** Returnキータイプは、選択したキーボードタイプに基づきますが、アプリで妥当だと判断できる場合は変更できます。例えば、アプリで検索を開始する場合、ユーザが他の場所で検索を開始する場合と体験が統一されるように、標準のReturnキータイプではなく、検索用のReturnキータイプを使用することができます。デベロッパ向けのガイダンスは、[`submitLabel(_:)`](/documentation/SwiftUI/View/submitLabel\(_:\))（SwiftUI）および[`UIReturnKeyType`](/documentation/UIKit/UIReturnKeyType)（UIKit）を参照してください。

## [カスタム入力ビュー](/jp/design/human-interface-guidelines/virtual-keyboards#Custom-input-views)

アプリでのデータ入力タスクを拡張するカスタム機能を提供したい場合は、必要に応じて _入力ビュー_ を作成できます。例えばNumbersでは、スプレッドシートの編集時に数値入力用のカスタム入力ビューが表示されます。ユーザがアプリを使用している間、システムが提供するキーボードの代わりにカスタム入力ビューが表示されます。デベロッパ向けのガイダンスは、[`ToolbarItemPlacement`](/documentation/SwiftUI/ToolbarItemPlacement)（SwiftUI）および[`inputViewController`](/documentation/UIKit/UIResponder/inputViewController)（UIKit）を参照してください。

**カスタム入力ビューがアプリのコンテキストに適合しているか確認する。** データ入力をシンプルかつ直感的にするだけでなく、ユーザにカスタム入力ビューを使用するメリットを理解してもらうようにします。そうしないと、ユーザはなぜアプリでシステムのキーボードに戻せないのか疑問に思うかもしれません。

**ユーザの入力時に標準のキーボードのサウンドを再生する。** キーボードのサウンドは、ユーザがシステムのキーボードのキーをタップしたときにおなじみのフィードバックを提供します。そのため、ユーザはカスタム入力ビューのキーをタップしたときも同じサウンドが再生されることを期待します。ユーザは、「設定」＞「サウンド」で、すべてのキーボード操作のキーボードサウンドをオフにできます。デベロッパ向けのガイダンスは、[`playInputClick()`](/documentation/UIKit/UIDevice/playInputClick\(\))（UIKit）を参照してください。

## [カスタムキーボード](/jp/design/human-interface-guidelines/virtual-keyboards#Custom-keyboards)

iOS、iPadOS、tvOSでは、アプリ機能拡張を作成することで、システムキーボードに代わるカスタムキーボードを提供できます。 _アプリ機能拡張_ は、デベロッパからユーザに提供されるインストール可能なコードで、システムの特定の領域の機能を拡張します。詳しくは、[アプリ機能拡張](https://developer.apple.com/app-extensions/)を参照してください。

ユーザは「設定」でカスタムキーボードを選択して、任意のアプリでのテキスト入力に使用できます。ただし、セキュリティで保護されたテキストフィールドと電話番号フィールドを編集する場合は除きます。ユーザは複数のカスタムキーボードを選択でき、いつでも切り替えられます。デベロッパ向けのガイダンスは、[カスタムキーボードの作成](/documentation/UIKit/creating-a-custom-keyboard)を参照してください。

カスタムキーボードは、ほかにはないキーボード機能をシステム全体に提供したい場合に適しています。例えば、テキストを入力する斬新な方法を提供したり、システムが対応していない言語でタイプできるようにしたりする場合です。アプリの中でのみ使用できるカスタムキーボードを提供したい場合は、カスタム入力ビューを作成することをおすすめします。

**明確かつ簡単な方法でキーボードを切り替えられるようにする。** 標準キーボードでは、複数のキーボードが使用可能な場合に、専用の絵文字キーに代わって地球儀キーが表示されます。ユーザは、これを使用して素早く別のキーボードに切り替えられることを知っており、当然、カスタムのキーボードでも同じ直感的な操作ができると考えます。

**システムが提供するキーボード機能を複製しない。** 一部のデバイスでは、ユーザがカスタムキーボードを使用している場合でも、キーボードの下に絵文字/地球儀キーと音声入力キーが自動的に表示されます。これらのキーはアプリから制御できません。カスタムキーボードでこれらのキーと見た目が同じキーを表示すると、ユーザが戸惑う可能性があります。

**アプリでキーボードのチュートリアルを提供する。** ユーザは標準キーボードに慣れており、新しいキーボードの使い方の習得に時間がかかる可能性があります。アプリに使い方のチュートリアルを表示すれば、このプロセスを簡単にするのに役立ちます。トピックとして例えば、カスタムキーボードを選択する方法、テキストの入力中に有効にする方法、使用する方法、標準のキーボードに戻す方法が考えられます。キーボード自体にヘルプコンテンツを表示しないでください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/virtual-keyboards#Platform-considerations)

 _macOSには対応していません。_

### [iOS/iPadOS](/jp/design/human-interface-guidelines/virtual-keyboards#iOS-iPadOS)

**キーボードレイアウトガイドを使用して、キーボードとインターフェイスの一体感を高める。** レイアウトガイドを使用すれば、画面に仮想キーボードが表示されている間もインターフェイスのほかの重要な部分が隠れないようにすることができます。デベロッパ向けのガイダンスは、[キーボードレイアウトガイドでレイアウトを調整する](/documentation/UIKit/adjusting-your-layout-with-keyboard-layout-guide)を参照してください。

![iPhoneアプリのレイアウト図。キーボードの上に、2つのテキストフィールドとボタンが縦に重なって表示されています。](https://docs-assets.developer.apple.com/published/2d310619deb1ce3587596b7fee6e5b08/ui-fully-visible%402x.png)

![丸に囲まれたチェックマークが適切な例であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)キーボードレイアウトガイドを使用すると、アプリのUIとキーボードがうまく連係して動作します。

![iPhoneアプリのレイアウト図。縦に重なった2つのテキストフィールドが表示されています。キーボードが下の方のテキストフィールドの一部を覆っています。](https://docs-assets.developer.apple.com/published/b2612a1b69632d398d2744caee9ff1e2/text-field-hidden%402x.png)

![丸に囲まれたX印が不適切な例であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)キーボードレイアウトガイドを使用しないと、テキストを入力しにくくなります。

![iPhoneアプリのレイアウト図。キーボードの上に、2つのテキストフィールドとボタンが縦に重なって表示されています。キーボードがボタンの一部を覆っています。](https://docs-assets.developer.apple.com/published/3a2b1c460427926e69f4d3e8d1383aef/button-hidden%402x.png)

![丸に囲まれたX印が不適切な例であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)キーボードレイアウトガイドを使用しないと、ボタンをタップしにくくなります。

**カスタムコントロールは、キーボードの上に慎重に配置する。** 一部のアプリでは、ユーザが操作しているデータに関連するアプリ固有の機能を提供するために、キーボードの上にカスタムコントロールを含む入力アクセサリビューが配置されます。例えばNumbersでは、スプレッドシートのデータに標準またはカスタムの計算を適用できるコントロールが表示されます。アプリにキーボードを拡張するカスタムコントロールを用意する場合は、そのコントロールが現在のタスクに関連していることを確認してください。アプリ内の他のビューでLiquid Glassを使用している場合、またはキーボードの上でビューが不自然に表示される場合は、コントロールを含むビューにLiquid Glassを適用して一貫性を保ちます。標準のツールバーを使用してコントロールを表示している場合は、自動的にLiquid Glassが採用されます。キーボードレイアウトガイドと標準のパディングを使用して、コントロールがビュー内で想定通りに配置されるようにしてください。デベロッパ向けのガイダンスは、[`ToolbarItemPlacement`](/documentation/SwiftUI/ToolbarItemPlacement)（SwiftUI）、[`inputAccessoryView`](/documentation/UIKit/UIResponder/inputAccessoryView)（UIKit）、および[`UIKeyboardLayoutGuide`](/documentation/UIKit/UIKeyboardLayoutGuide)（UIKit）を参照してください。

### [tvOS](/jp/design/human-interface-guidelines/virtual-keyboards#tvOS)

tvOSでは、Siri Remoteでテキストフィールドを選択したときに、文字が横に並んだ仮想キーボードが表示されます。

備考

Siri Remote以外のデバイスを使用している場合は、グリッドキーボード画面が表示され、コンテンツのレイアウトがキーボードに合わせて自動的に調整されます。

ユーザが数字入力ビューを呼び出すと、数字専用キーボードが表示されます。ガイダンスは[数字入力ビュー](/jp/design/human-interface-guidelines/digit-entry-views)を参照してください。

### [visionOS](/jp/design/human-interface-guidelines/virtual-keyboards#visionOS)

visionOSでは、システム提供の仮想キーボードが直接的ジェスチャと間接的ジェスチャの両方に対応し、ユーザが好きな場所に移動できる別個のウインドウに表示されます。レイアウト内にキーボードの場所を確保しておく必要はありません。

以下のカスタムコントロールを使用できます 

このビデオコンテンツの説明: visionOSの仮想キーボードでタイピングしている人を映した録画。 

再生 

### [watchOS](/jp/design/human-interface-guidelines/virtual-keyboards#watchOS)

Apple Watchでは、デバイスの画面が十分に大きい場合、テキストフィールドにキーボードを表示できます。それ以外の場合、ユーザは音声入力またはスクリブルを使用して情報を入力できます。watchOSではキーボードタイプを変更することはできませんが、テキストフィールドのコンテンツタイプを設定することはできます。システムでは、この情報を使用して候補を表示するなどにより、テキスト入力を簡単にします。デベロッパ向けのガイダンスは、[`textContentType(_:)`](/documentation/SwiftUI/View/textContentType\(_:\))（SwiftUI）を参照してください。

ユーザは、近くにあるペアリング済みのiPhoneを使用して、Apple Watchでテキストを入力することもできます。

## [リソース](/jp/design/human-interface-guidelines/virtual-keyboards#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/virtual-keyboards#Related)

[データの入力](/jp/design/human-interface-guidelines/entering-data)

[キーボード](/jp/design/human-interface-guidelines/keyboards)

[レイアウト](/jp/design/human-interface-guidelines/layout)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/virtual-keyboards#Developer-documentation)

[`keyboardType(_:)`](/documentation/SwiftUI/View/keyboardType\(_:\)) — SwiftUI

[`textContentType(_:)`](/documentation/SwiftUI/View/textContentType\(_:\)) — SwiftUI

[`UIKeyboardType`](/documentation/UIKit/UIKeyboardType) — UIKit

## [変更履歴](/jp/design/human-interface-guidelines/virtual-keyboards#Change-log)

日付| 変更内容  
---|---  
2025年6月09日| キーボードの上にカスタムコントロールを表示する際のガイダンスを追加し、watchOSでの仮想キーボードの対応状況を反映するように更新。  
2024年2月02日| visionOSでの仮想キーボードの直接的ジェスチャと間接的ジェスチャの対応を明確化。  
2023年12月05日| visionOSのアートワークを追加。  
2023年6月21日| 「オンスクリーンキーボード」からページタイトルを変更、visionOSのガイダンスを追加するために更新。
