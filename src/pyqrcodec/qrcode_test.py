#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2014年7月22日

@author: cosimzhou
'''

from qrcode import *
import unittest

outputDir = '../../output'

class TestQRCode(unittest.TestCase):
    @staticmethod
    def setUpClass():
        print "setUp TestQRCode unittest."
    @staticmethod
    def tearDownClass():
        print "tearDown TestQRCode unittest."
    def setUp(self):
        print "setUp TestQRCode one case."
    def tearDown(self):
        print "tearDown TestQRCode one case."
    def test_add(self):
        pass
    def test_QREncode(self):
        raw = 'https://github.com/Cosimzhou/pyqrcode'
        qrc = QREncode(raw, level='L')
        qrc.outputMatrixPicture('%s/output-l.png'%outputDir, margin=10)

        qrc = QREncode(raw, level='M')
        qrc.outputMatrixPicture('%s/output-m.png'%outputDir)

        qrc = QREncode(raw, level='Q')
        qrc.outputMatrixPicture('%s/output-q.png'%outputDir)

        qrc = QREncode(raw, level='H')
        qrc.outputMatrixPicture('%s/output-h.png'%outputDir, grid=True)

        qrc.printOnConsole()
        self.assertEqual(0, 0)

    def test_simpleQREncode(self):
        data = 'https://github.com/Cosimzhou/pyqrcode'
        mode = QRDataEncoder.chooseMode(data)
        level = 'L'

        qrd = QRDataEncoder()
        qrc = QRCoder()
        qrd.setMode(mode)
        while True:
            ldata = qrd.assumeLength(data)
            lbyte = ldata / 8 + (1 if ldata % 8 else 0)
            vq = qrc.getVersionAndQualityByDataLength(lbyte, level)
            vdiff = qrd.isFitVersion(vq[0])
            if vdiff == 0:
                break
            qrd.shiftVersion(vdiff)

        qrc.beginACode(*vq)
        prdata = qrd.encodeData(data)
        pinfo = qrc.piecesInfo()
        print qrc.dataCaps(), qrc.checkCodeLength()
        prdata = qrd.fillContent(prdata, qrc.dataCaps())
        datas = qrd.encodeBlocksCheckCode(prdata, pinfo)
        print datas



        minscore, minmask = INF, 0
        for mask in xrange(8):
            qrc.Mask = mask
            qrc.fillData(datas)
            qrc.setFormatInfo()

            score = qrc.evaluate()
            if score < minscore:
                minscore, minmask = score, mask

            qrc.outputMatrixPicture('%s/test-%s.png'%(outputDir,mask), grid = True)

        print 'Best index: %s, %s'%(minmask, minscore)

        qrc.Mask = minmask
        qrc.fillData(datas)
        qrc.setFormatInfo()

        print qrc
        qrc.printOnConsole()

        print qrc[6][7]

        info = qrc.getInfo()
        for key in info:
            print '%s: %s'%(key, info[key])

        import shutil
        shutil.copy('%s/test-%s.png'%(outputDir,minmask), '%s/test.png'%outputDir)

    def test_extractData(self):
        qrd = QRDataEncoder(mode=mode, quality=level)
        qrd.encode(data)

        qrc = QRCoder()
        qrc.beginACode(qrd.version, qrd.quality)
        qrc.chooseAMask(qrd.data)
        qrc.fillData(qrd.data)
        qrc.setFormatInfo()

        ds = qrc.extractData()

        assert len(ds) == len(qrd.data)
        for i in xrange(len(ds)):
            if ds[i] == qrd.data[i]:
                pass
            else:
                print "bad", i, len(ds[i]), len(qrd.data[i]), ds[i],qrd.data[i]


    @unittest.skipIf(1, "")
    def test_draw_mask_code(self):
        for v in xrange(1,41):
            for i in xrange(8):
                qrc = drawMaskCode(v, i)
                qrc.outputMatrixPicture('%s/test-s@%s-%s.png'%(outputDir, v, i))

    @unittest.skipIf(1, "")
    def test_drawBlockColor(self):
        for v in xrange(1, 41):
            qrc = drawBlockColor(v, 0)
            qrc.outputMatrixPicture('%s/test-x@%s.png'%(outputDir, v))


if __name__ == '__main__':
    unittest.main()
