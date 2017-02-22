<?php
/**
 * Y!mobileで通信速度を低速化された時、通信速度を通常に戻す申し込みを実行するスクリプトです。
 * スクレイピングライブラリとして、Goutte(https://github.com/FriendsOfPHP/Goutte)を使用しています. composerでダウンロードして下さい。
 *
 * [実行コマンド]
 * php Automator.php 電話番号 パスワード 契約番号
 *
 * 例: php Automator.php 08012345678 passwrod 1234567890
 * (電話番号が'080-1234-5678'、パスワードが'passwrod'、契約番号が'1234567890'だとする)
 *
 * Created by M.Inaba
 * Date: 2015/11/26
 * Copyright (c) 2015- M.Inaba
 * This program is licensed under the MIT license.
 */
require_once __DIR__ . '/vendor/autoload.php';
use Goutte\Client;

date_default_timezone_set('Asia/Tokyo');
(new Automator())->execute($argv[1], $argv[2], $argv[3]);

class Automator {
    const URL = 'https://webmy.ymobile.jp';

    private $client;

    public function Automator() {
        $this->client = new Client();
    }

    public function execute($tel, $password, $contract_code) {
        // ログイン画面に遷移
        $this->client->request('GET', self::URL . '/portal/loginMsn/');

        // 電話番号とパスワードでログイン
        $this->client->request('POST', self::URL . '/portal/loginMsn/login', $this->get_login_params($tel, $password));

        // オンラインサポート画面に遷移(別タブ)
        $this->client->request('POST', self::URL . '/portal/home/openOnlineSupport', $this->get_online_support_params($contract_code));

        // 契約内容照会画面に遷移
        $this->client->request('POST', self::URL . '/web/contract/toContract/', $this->get_default_params());

        // 「通常速度に戻すお申し込み・ご利用データ通信量の確認」画面に遷移
        $this->client->request('POST', self::URL . '/web/dualService/index/', $this->get_default_params());

        // 「4G通常速度に戻すお申し込み・予約解除」画面に遷移
        $this->client->request('POST', self::URL . '/web/dualService/request/', $this->get_default_params());

        // 申込内容を入力
        $this->client->request('POST', self::URL . '/web/dualService/confirm/', $this->get_apply_params());

        // 申込の実行
        $this->client->request('POST', self::URL . '/web/dualService/update/', $this->get_default_params());
    }

    private function get_login_params($tel, $password) {
        $crawler = $this->client->getCrawler();

        return [
            'msisdn'           => $tel,
            'password'         => $password,
            'messageDigest'    => $crawler->filter('input[name=messageDigest]')->attr('value'),
            'pageId'           => $crawler->filter('#pageId')->attr('value'),
            'loginDisplayCode' => $crawler->filter('#loginDisplayCode')->attr('value'),
        ];
    }

    private function get_online_support_params($contract_code) {
        $crawler = $this->client->getCrawler();

        return [
            'selectedKeiyakuCd'                   => $contract_code,
            'messageDigest'                       => $crawler->filter('input[name=messageDigest]')->attr('value'),
            'pageId'                              => $crawler->filter('#pageId')->attr('value'),
            'loginDisplayCode'                    => $crawler->filter('#loginDisplayCode')->attr('value'),
            'portalAccountId'                     => $crawler->filter('input[name=portalAccountId]')->attr('value'),
            'org.apache.struts.taglib.html.TOKEN' => $crawler->filter('input[name="org.apache.struts.taglib.html.TOKEN"]')->attr('value'),
        ];
    }

    private function get_default_params() {
        $crawler = $this->client->getCrawler();

        return [
            'userName'                            => $crawler->filter('input[name=userName]')->attr('value'),
            'functionName'                        => $crawler->filter('input[name=functionName]')->attr('value'),
            'pageTitle'                           => $crawler->filter('input[name=pageTitle]')->attr('value'),
            'pageName'                            => $crawler->filter('input[name=pageName]')->attr('value'),
            'pageId'                              => $crawler->filter('input[name=pageId]')->attr('value'),
            'contractorCode'                      => $crawler->filter('input[name=contractorCode]')->attr('value'),
            'org.apache.struts.taglib.html.TOKEN' => $crawler->filter('input[name="org.apache.struts.taglib.html.TOKEN"]')->attr('value'),
            'formTimestamp'                       => $crawler->filter('input[name=formTimestamp]')->attr('value'),
        ];
    }

    private function get_apply_params() {
        $crawler = $this->client->getCrawler();

        $apply_status = $crawler->filter('#selectedRequestStatus')->filter('option')->eq(1)->attr('value');

        $now = date('Y/m/d (D) H:i:s', time());
        if ($apply_status == '10') {
            print_r("{$now}: Apply immediately.\n");
        } else if ($apply_status == '11') {
            print_r("{$now}: Apply reservation.\n");
        } else if ($apply_status == '12') {
            print_r("{$now}: Already reserved.\n");
            exit;
        }

        return array_merge($this->get_default_params(), ['selectedRequestStatus' => $apply_status]);
    }
}
