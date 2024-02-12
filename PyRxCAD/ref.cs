public static Point3d PolarPoint(Point3d basepoint, double angle, double distance)
{
    // credits to Tony Tanzillo
    return new Point3d(
    basepoint.X + (distance * Math.Cos(angle)),
    basepoint.Y + (distance * Math.Sin(angle)),
    basepoint.Z);
}
[CommandMethod("PARC")]
public void addArcs()
{

    Document doc = Autodesk.AutoCAD.ApplicationServices.Application.DocumentManager.MdiActiveDocument;

    Editor ed = doc.Editor;

    Database db = doc.Database;

    Transaction tr = doc.TransactionManager.StartTransaction();

    using (tr)
    {
        BlockTableRecord btr = (BlockTableRecord)tr.GetObject(db.CurrentSpaceId, OpenMode.ForWrite);
        // prompt for selecting polyline   
        PromptEntityOptions peo = new PromptEntityOptions("\nSelect a polyline: >>");

        peo.SetRejectMessage("\nSelect a polyline only >>");

        peo.AddAllowedClass(typeof(Polyline), false);

        peo.AllowObjectOnLockedLayer = true;

        PromptEntityResult res;

        res = ed.GetEntity(peo);

        if (res.Status != PromptStatus.OK) return;

        Entity ent = (Entity)tr.GetObject(res.ObjectId, OpenMode.ForRead);

        if (ent == null) return;

        Polyline pline = (Polyline)ent as Polyline;

        if (pline == null) return;

        // get the number of segments   

        int segments = pline.NumberOfVertices - 1;

        for (int i = 0; i < segments; i++)
        {
            if (pline.GetSegmentType(i) == SegmentType.Arc)

                continue;

            // get arc segment on polyline   
            LineSegment2d lseg = pline.GetLineSegment2dAt(i);

            // get center   

            Point2d center = lseg.EvaluatePoint(0.5);
            // create an Arc   
            Point2d p1 = lseg.StartPoint;
            Point2d p2 = lseg.EndPoint;
            double ang = lseg.Direction.Angle;
            Point3d mp = new Point3d((p1.X + p2.X) / 2, (p1.Y + p2.Y) / 2, pline.Elevation).TransformBy(Matrix3d.Identity);
            // get half of hord
            double cat = lseg.Length / 2.0;
            // you have soecify radius of an arc here:
            double rad = lseg.Length * 1.25;// <--    dummy radius for test
                                            // get next catet
            double bcat = Math.Sqrt(rad * rad - cat * cat);

            Point3d cp = PolarPoint(mp, ang + Math.PI / 2, bcat);

            Plane plan = new Plane(Point3d.Origin, Vector3d.ZAxis);

            Point3d sp = new Point3d(p1.X, p1.Y, pline.Elevation);

            Point3d ep = new Point3d(p2.X, p2.Y, pline.Elevation);

            // create arc using center radius and both angles, count clockwise from start line to end
            Arc arc = new Arc(cp, rad, cp.GetVectorTo(sp).AngleOnPlane(plan), cp.GetVectorTo(ep).AngleOnPlane(plan));

            // add to current space and transaction
            btr.AppendEntity(arc);

            tr.AddNewlyCreatedDBObject(arc, true);


        }
        tr.Commit();
    }

}