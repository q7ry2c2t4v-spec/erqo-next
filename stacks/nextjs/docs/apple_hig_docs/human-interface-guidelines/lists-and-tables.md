# リストとテーブル

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/lists-and-tables

# リストとテーブル

リストとテーブルでは、行に対して1つ以上の列にデータが表示されます。

![ヘッダとフッタのテキストを持つ、図案化された3行の表。画像は6色のオリジナルAppleロゴをイメージさせる赤色になっています。](https://docs-assets.developer.apple.com/published/907c40e1a41672f0e62b74c4f61c0f9c/components-lists-and-tables-intro%402x.png)

テーブルまたはリストでは、グループや階層に整理されたデータを示すことができ、選択、追加、削除、並べ替えなどのユーザ操作に対応できます。すべてのプラットフォームのアプリやゲームで、テーブルを使ってコンテンツやオプションを表示できます。多くのアプリでは、全体的な情報の階層を表現し、階層内を移動しやすくするためにリストが使用されます。例えば、iOSの「設定」ではユーザがオプションを選択できるようにリストの階層が使用され、iPadOSおよびmacOSの「メール」などの複数のアプリでは[分割ビュー](https://developer.apple.com/jp/design/human-interface-guidelines/split-views)内でテーブルが使用されます。

複数列のテーブルやスプレッドシートでユーザが複雑なデータを操作しなければならない場合があります。生産性向上のタスクを提供するアプリでは、並べ替え可能な個別の列にデータのさまざまな特性や属性を表示する目的でテーブルがよく使用されます。

## [ベストプラクティス](/jp/design/human-interface-guidelines/lists-and-tables#Best-practices)

**リストまたはテーブルではテキストの表示を優先する。** テーブルにはあらゆる種類のコンテンツを表示できますが、行ベースのフォーマットはテキストをスキャンしたり読んだりしやすくする目的に特に適しています。サイズのばらつきの大きい項目がある場合、または多数の画像を表示する必要がある場合は、代わりに[コレクション](https://developer.apple.com/jp/design/human-interface-guidelines/collections)を使用することを検討してください。

**適切な場合に限りユーザがテーブルを編集できるようにする。** ユーザは、リストの項目の追加や削除ができなくても、並べ替えができればありがたいと感じます。iOSおよびiPadOSでは、ユーザがテーブルの項目を選択するには編集モードに切り替える必要があります。

**ユーザがリストの項目を選択したときに適切なフィードバックを提供する。** 項目を選択したときに新しいビューが開くか、項目の状態が切り替わるかに応じて、異なるフィードバックを提供できます。一般に、階層内を移動するためのテーブルでは、ユーザがたどっているパスを明確にするために選択済みの行が常に強調表示されます。これに対し、オプションがリスト表示されるテーブルでは、多くの場合行が短時間だけ強調表示されてから、項目が選択されたことを示すチェックマークなどの画像が追加されます。

## [コンテンツ](/jp/design/human-interface-guidelines/lists-and-tables#Content)

**常に項目のテキストを簡潔にして行の内容を読みやすくする。** 短く簡潔なテキストにするとテキスト切れや折り返しを最低限にとどめることができ、テキストを読んだりスキャンしたりしやすくなります。各項目が大量のテキストで構成される場合は、大きすぎるテーブルの行の表示を避けるための代替手段を検討してください。例えば、項目のタイトルのみをリスト表示して、ユーザが項目を選択してその内容を詳細ビューに表示できるようにします。

**ほかの方法では収まりきらなかったり切れたりする可能性があるテキストの読みやすさを保つ方法を検討する。** ユーザがテーブルの幅を変更できる場合などにテーブルが狭くなっても、内容を認識でき、簡単に読めるようにする必要があります。テキストの中央に省略記号を表示すると、内容の先頭と末尾の両方が保持されるため、項目を区別しやすくなります。

**複数列のテーブルでは説明的な列見出しを使用する。**[タイトルスタイルの大文字設定](https://support.apple.com/guide/applestyleguide/c-apsgb744e4a3/web#apdca93e113f1d64)を適用した名詞や短い名詞フレーズを使用します。末尾には句読点を追加しないでください。1列のテーブルビューに列見出しを含めない場合は、ユーザがコンテキストを理解できるようにラベルまたはヘッダを使用します。

## [スタイル](/jp/design/human-interface-guidelines/lists-and-tables#Style)

**データおよびプラットフォームと調和するテーブルまたはリストのスタイルを選ぶ。** 一部のスタイルでは、特定の体験を提供するために、視覚的な詳細度を使ってグループや階層が伝えられます。例えばiOSおよびiPadOSでは、グループ化スタイルでヘッダ、フッタ、およびデータのグループを区切る追加のスペースが使用されます。watchOSで使用できる楕円スタイルでは、ユーザがスクロールしたときに項目が丸みのある面に沿って回転して消えていくように表示されます。macOSでは、行の背景を交互に変えて大きなテーブルを使いやすくするボーダースタイルが定義されています。デベロッパ向けのガイダンスは、[`ListStyle`](/documentation/SwiftUI/ListStyle)を参照してください。

**表示する必要がある情報に適した行のスタイルを選ぶ。** 例えば、行の先頭に小さい画像、その後ろに短い説明ラベルの表示が必要な場合があります。一部のプラットフォームでは、リストの行にコンテンツを配置できるビルトインの行のスタイルが提供されています。例えば、iOS、iPadOS、tvOSではコンテンツをリストの行、ヘッダ、フッタにレイアウトするために使用できる[`UIListContentConfiguration`](/documentation/UIKit/UIListContentConfiguration-swift.struct) APIが提供されています。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/lists-and-tables#Platform-considerations)

### [iOS、iPadOS、visionOS](/jp/design/human-interface-guidelines/lists-and-tables#iOS-iPadOS-visionOS)

**情報ボタンは行のコンテンツの詳細情報を表示するためにのみ使用する。** 情報ボタン（リストの行に表示される場合は _詳細開閉用ボタン_ と呼ばれます）では、階層型のテーブルまたはリスト内での移動はできません。ユーザがリストまたはテーブルの行のサブビューまでドリルダウンできるようにする必要がある場合は、開閉用インジケータのアクセサリコントロールを使用します。デベロッパ向けのガイダンスは、[`UITableViewCell.AccessoryType.disclosureIndicator`](/documentation/UIKit/UITableViewCell/AccessoryType-swift.enum/disclosureIndicator)を参照してください。

![グループ化された行のリストの図。各リスト項目の行の末尾には情報ボタンが含まれています。](https://docs-assets.developer.apple.com/published/eafd931e48db1cb4b4c9869900b71e29/info-button-in-list%402x.png)情報ボタンをタップすると、リスト項目の詳細が表示されますが、移動はできません。

![グループ化された行のリストの図。各リスト項目の行の末尾には右向きのシェブロンが含まれています。](https://docs-assets.developer.apple.com/published/aaeb1e2c8c7919f96b584931f1b2605b/disclosure-indicator-in-list%402x.png)開閉用インジケータをタップすると、階層の次のレベルが表示されます。項目の詳細は表示されません。

**行の末尾に開閉用インジケータなどのコントロールが表示されるテーブルにはインデックスを追加しない。** _インデックス_ は一般にアルファベットの文字で構成され、リストの右に縦に並べて表示されます。ユーザがインデックスの文字を選択すると、その文字に対応する特定のセクションにジャンプできます。インデックスと開閉用インジケータなどの要素はどちらもリストの右側に表示されるため、ユーザが一方の要素を作動させずに他方を使用することが困難になる場合があります。

### [macOS](/jp/design/human-interface-guidelines/lists-and-tables#macOS)

**値が表示される場合は、ユーザが列見出しをクリックしてその列を基準にテーブルビューを並べ替えられるようにする。** ユーザがすでに並べ替えた列の見出しをクリックした場合は、データを逆順に並べ替えます。

**ユーザが列の幅を変更できるようにする。** 多くの場合、テーブルビューに表示されるデータの幅はまちまちです。ユーザがさまざまな領域に注目したり、収まりきらなかったデータを表示したりできるように、列のサイズを変更可能にすると喜ばれます。

**複数列の表では行のカラーを交互にすることを検討する。** カラーを交互にすると、特に幅の広いテーブルの場合に、ユーザが複数の列をまたいで行の値を追いやすくなります。

**階層型のデータの表示にはテーブルビューではなくアウトラインビューを使用する。**[アウトラインビュー](https://developer.apple.com/jp/design/human-interface-guidelines/outline-views)はテーブルビューに似た見た目ですが、入れ子にしたデータのレベルを表示するための開閉用三角ボタンが含まれます。例えば、アウトラインビューにフォルダとその中の項目を表示できます。

### [tvOS](/jp/design/human-interface-guidelines/lists-and-tables#tvOS)

**フォーカスが置かれたときに各行が強調表示されて少し大きくなっても、テーブルの近くにある画像が適切に表示されることを確認する。** フォーカスが置かれた行の角が丸められることもあり、それが左側または右側にある画像の表示に影響する場合があります。画像を準備するときはこの影響を考慮に入れ、角を丸めるために独自のマスクを追加しないでください。

### [watchOS](/jp/design/human-interface-guidelines/lists-and-tables#watchOS)

**なるべく行数を少なくする。** 短いリストの方が全体をざっと見るのには適していますが、長い項目リストの方が望ましい場合もあります。例えば、たくさんのポッドキャストのサブスクリプションを登録しようとするときに、すべての項目が見えないとユーザは何かがおかしいと思うかもしれません。最も関連性の高い項目だけをリストに表示し、より多くの項目を表示する方法を提供することで、長いリストを扱いやすくできます。

**縦長のページを使用するナビゲーションに対応する場合は、詳細ビューの長さを制限する。** 縦方向のページナビゲーションを使うと、リスト行の詳細項目間を縦スワイプで移動することができます。このナビゲーション方法は、わざわざリストに戻って次の詳細項目をタップする必要がないので時間の節約になりますが、詳細ビューが短いときしか使えません。詳細ビューがスクロールする場合は、縦方向のページナビゲーションで項目間をスワイプで移動できないためです。

## [リソース](/jp/design/human-interface-guidelines/lists-and-tables#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/lists-and-tables#Related)

[コレクション](/jp/design/human-interface-guidelines/collections)

[アウトラインビュー](/jp/design/human-interface-guidelines/outline-views)

[レイアウト](/jp/design/human-interface-guidelines/layout)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/lists-and-tables#Developer-documentation)

[`List`](/documentation/SwiftUI/List) — SwiftUI

[テーブル](/documentation/SwiftUI/Tables) — SwiftUI

[`UITableView`](/documentation/UIKit/UITableView) — UIKit

[`NSTableView`](/documentation/AppKit/NSTableView) — AppKit

#### [ビデオ](/jp/design/human-interface-guidelines/lists-and-tables#Videos)

[](https://developer.apple.com/videos/play/wwdc2020/10031)

## [変更履歴](/jp/design/human-interface-guidelines/lists-and-tables#Change-log)

日付| 変更内容  
---|---  
2023年6月21日| visionOSのガイダンスを追加するために更新。  
2023年6月05日| watchOS 10の変更点を反映するためにガイダンスを更新。
