// (C) Copyright 2002-2013 by Autodesk, Inc. 
//
// Permission to use, copy, modify, and distribute this software in
// object code form for any purpose and without fee is hereby granted, 
// provided that the above copyright notice appears in all copies and 
// that both that copyright notice and the limited warranty and
// restricted rights notice below appear in all supporting 
// documentation.
//
// AUTODESK PROVIDES THIS PROGRAM "AS IS" AND WITH ALL FAULTS. 
// AUTODESK SPECIFICALLY DISCLAIMS ANY IMPLIED WARRANTY OF
// MERCHANTABILITY OR FITNESS FOR A PARTICULAR USE.  AUTODESK, INC. 
// DOES NOT WARRANT THAT THE OPERATION OF THE PROGRAM WILL BE
// UNINTERRUPTED OR ERROR FREE.
//
// Use, duplication, or disclosure by the U.S. Government is subject to 
// restrictions set forth in FAR 52.227-19 (Commercial Computer
// Software - Restricted Rights) and DFAR 252.227-7013(c)(1)(ii)
// (Rights in Technical Data and Computer Software), as applicable.
//

//-----------------------------------------------------------------------------
//----- acrxEntryPoint.cpp
//-----------------------------------------------------------------------------
#include "StdAfx.h"
#include "resource.h"
#include "acjs.h"  //requires linking to "AcJsCoreStub_crx.lib"


//-----------------------------------------------------------------------------
#define szRDS _RXST("asdk")

//-----------------------------------------------------------------------------

Acad::ErrorStatus postToDatabase (AcDbEntity *pEnt, AcDbObjectId &idObj) 
{
	Acad::ErrorStatus es;

	AcDbDatabase* pDb = acdbHostApplicationServices()->workingDatabase();

	AcDbBlockTablePointer blkTable(pDb, AcDb::kForRead);

	if((es = blkTable.openStatus()) != Acad::eOk)
		return es;

	AcDbBlockTableRecordPointer btr(
		ACDB_MODEL_SPACE, 
		pDb, 
		AcDb::kForWrite);

	if((es = btr.openStatus()) != Acad::eOk)
		return es;

	return btr->appendAcDbEntity(idObj, pEnt);
}

// An ARX method that can be invoked from JavaScript 
// needs to have the following signature:
// char* MethodName(const char* args)
//  - args: a json formatted string containing the arguments
//  - return type: a json formatted string containing a "retCode"
//  member + any custom members you may need.
char* TestArxRead(const char* args)
{
	acutPrintf (L"\nTestArxRead") ;

	Acad::ErrorStatus es;

	AcDbDatabase* pDb = acdbHostApplicationServices()->workingDatabase();

	AcDbBlockTableRecordPointer btr(
		ACDB_MODEL_SPACE, 
		pDb, 
		AcDb::kForRead);

	AcDbBlockTableRecordIterator *pBtrIter ;

	btr->newIterator (pBtrIter);

	for (; !pBtrIter->done(); pBtrIter->step())
	{
		AcDbObjectId id;
		es = pBtrIter->getEntityId(id);

		const ACHAR* name = id.objectClass()->name();

		acutPrintf (L"\n-Entity: %s", name) ;
	}

	delete pBtrIter;

	const char* res = "{\"retCode\":0, \"result\":\"OK\"}";

	return _strdup(res);  
}

void DocLock()
{
	AcDbDatabase *pDb = acdbHostApplicationServices()->workingDatabase(); 
	AcApDocument* pDoc = acDocManager->document(pDb); 
	acDocManager->lockDocument(pDoc, AcAp::kWrite);
}

void DocUnlock()
{
	AcDbDatabase *pDb = acdbHostApplicationServices()->workingDatabase(); 
	AcApDocument* pDoc = acDocManager->document(pDb); 
	acDocManager->unlockDocument(pDoc);
}

// A JavaScript invokated method needs to lock the document if 
// performing any modification
char* TestArxWrite(const char* args)
{
	acutPrintf (L"\nTestArxWrite");

	DocLock();

	Acad::ErrorStatus es;

	AcDbCircle* pCircle = new AcDbCircle(
		AcGePoint3d(0,0,0), 
		AcGeVector3d::kZAxis, 
		1.0);
	
	AcDbObjectId id;
	es = postToDatabase(pCircle, id);

	pCircle->close();

	DocUnlock();

	const char* res = "{\"retCode\":0, \"result\":\"OK\"}";

	return _strdup(res);  
}

//----- ObjectARX EntryPoint
class CArxJsTestApp : public AcRxArxApp {

public:
	CArxJsTestApp () : AcRxArxApp () {}

	virtual AcRx::AppRetCode On_kInitAppMsg (void *pkt) {
		// TODO: Load dependencies here

		// You *must* call On_kInitAppMsg here
		AcRx::AppRetCode retCode =AcRxArxApp::On_kInitAppMsg (pkt) ;
		
		// TODO: Add your initialization code here
		acjsDefun(L"TestArxRead", TestArxRead, ACJS_FUNC_INVOKEINDOC);
		acjsDefun(L"TestArxWrite", TestArxWrite, ACJS_FUNC_INVOKEINDOC);

		//ACJS_FUNC_INVOKEINDOC       0x00000001
		//ACJS_FUNC_INVOKESYNC        0x00000002
		//ACJS_FUNC_INVOKEASYNC       0x00000004
		
		return (retCode) ;
	}

	virtual AcRx::AppRetCode On_kUnloadAppMsg (void *pkt) {
		// TODO: Add your code here

		// You *must* call On_kUnloadAppMsg here
		AcRx::AppRetCode retCode =AcRxArxApp::On_kUnloadAppMsg (pkt) ;

		// TODO: Unload dependencies here

		return (retCode) ;
	}

	virtual void RegisterServerComponents () {

	}
	
	static void asdkMyGroupTestArxCmd () {
		acutPrintf(L"TestArxCmd...");
	}
} ;

//-----------------------------------------------------------------------------
IMPLEMENT_ARX_ENTRYPOINT(CArxJsTestApp)
ACED_ARXCOMMAND_ENTRY_AUTO(CArxJsTestApp, asdkMyGroup, TestArxCmd, MyCommandLocal, ACRX_CMD_MODAL, NULL)

