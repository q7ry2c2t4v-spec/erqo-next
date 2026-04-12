# カラム表示

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/column-views

# カラム表示

カラム表示（ _ブラウザ_ とも呼ばれる）では、縦方向のカラムを使用して、データ階層の参照や移動を行います。

![フォルダ、画像、ファイル情報のリストを含む3つの図案化されたカラム。画像は6色のオリジナルAppleロゴをイメージさせる赤色になっています。](https://docs-assets.developer.apple.com/published/a733ded25626efb9b0560ee646ef5763/components-column-view-intro%402x.png)

各カラムはデータ階層を構成する1つのレベルで、そこに含まれるデータ項目の横方向の行が表示されます。カラム内の項目が子項目を含む親項目の場合は、右向きの不等号が付きます。ユーザが親項目を選択すると、次のカラムにその子項目が表示されます。ユーザはこの操作を繰り返して、子項目を含まない項目に達するまで移動できます。親の階層に戻り、データのほかの分岐に移って同じように移動することもできます。

備考

iPadOSまたはvisionOSのアプリで階層構造のコンテンツの提示方法を管理する必要がある場合は、[分割ビュー](/jp/design/human-interface-guidelines/split-views)の使用を検討してください。

## [ベストプラクティス](/jp/design/human-interface-guidelines/column-views#Best-practices)

深いデータ階層内でユーザが頻繁に移動を繰り返すタイプのアプリで、[リストまたはテーブル](/jp/design/human-interface-guidelines/lists-and-tables)で提供されるような並べ替えの機能が必要ない場合は、カラム表示の使用を検討してください。例えばFinderは、ユーザがディレクトリ構造内を移動しやすいように、アイコン表示、リスト表示、ギャラリー表示に加えて、カラム表示に対応しています。

**データ階層のルートレベルを最初のカラムに表示する。** そうすれば、ユーザは最初のカラムまで素早く戻って、階層の一番上から移動を再開できます。

**子項目がない項目が選択されたら、その項目自体の情報を表示する。** 例えばFinderでは、選択された項目のプレビューと、作成日、変更日、ファイルタイプ、サイズなどの情報が表示されます。

**ユーザがカラムの幅を変更できるようにする。** デフォルトのカラム幅に入りきらない長い名前のデータ項目がある場合、この機能は特に重要です。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/column-views#Platform-considerations)

 _iOS、iPadOS、tvOS、visionOS、watchOSには対応していません。_

## [リソース](/jp/design/human-interface-guidelines/column-views#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/column-views#Related)

[リストとテーブル](/jp/design/human-interface-guidelines/lists-and-tables)

[アウトラインビュー](/jp/design/human-interface-guidelines/outline-views)

[分割ビュー](/jp/design/human-interface-guidelines/split-views)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/column-views#Developer-documentation)

[`NSBrowser`](/documentation/AppKit/NSBrowser) — AppKit
